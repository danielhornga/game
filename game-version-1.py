##Game Patch Number##

patchNumber = float(1.02)

##Check if file "UpdateIncomplete.txt" is present##
try:
    f = open("UpdateIncomplete.txt", "r")
except FileNotFoundError:
    ##Immediately Required Imports##

    import urllib.request
    import os
    import shutil
    import subprocess
    from subprocess import Popen
    import time
    import tkinter

    ##Fetch File For Most Recent Patch##

    path = os.getcwd()
    vLiveFilePath = path + "/Config/Live-Version.txt"
    url = "https://raw.githubusercontent.com/danielhornga/game/master/Live-Version"
    urllib.request.urlretrieve(url, vLiveFilePath)

    ##Compare Fetched File To Local Patch Number##

    f = open(vLiveFilePath, "r")
    LiveVersion = float(f.readline())
    f.close()
    os.remove(vLiveFilePath)

    if LiveVersion != patchNumber:

        def Update():
            ##File Path Re-Setup##
            cfilepath = path + "/Config"
            afilepath = path + "/Assets"
            gpath = path + "/game-version-1.py"
            gnpath = path + "/game-version-1-U.py"
            upath = path + "/Uninstaller.py"
            SecondPhaseFP = path + "/UpdateIncomplete.txt"
            shutil.rmtree(cfilepath)
            shutil.rmtree(afilepath)
            os.remove("Uninstaller.py")
            os.mkdir(cfilepath)
            os.mkdir(afilepath)

            ##Settings File Creation##
            sfname = os.path.join(cfilepath, "Settings.txt")
            f = open(sfname, "w+")
            f.write("Screen_Height:800\nScreen_Width:800\nFPS:244")
            f.close()

            ##Program web downloads##
            url = "https://raw.githubusercontent.com/danielhornga/game/master/game-version-1.py"
            urllib.request.urlretrieve(url, gnpath)
            url = "https://raw.githubusercontent.com/danielhornga/game/master/Uninstaller.py"
            urllib.request.urlretrieve(url, upath)

            ##Relaunch and second phase pass##
            f = open(SecondPhaseFP, "w+")
            f.close()
            process = subprocess.Popen(["python", gnpath])
            os.remove("game-version-1.py")
            quit()

    ##Setup animation loop variable##
    Animation = True

    ##Create 'Loading' Screen##
    LoadScreen = tkinter.Tk()
    WindowWidth = 750
    WindowHeight = 500
    ScreenWidth = LoadScreen.winfo_screenwidth()
    ScreenHeight = LoadScreen.winfo_screenheight()
    x = (ScreenWidth/2) - (WindowWidth/2)
    y = (ScreenHeight/2) - (WindowHeight/2)
    LoadScreen.title("")
    LoadScreen.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, x, y))
    LoadScreen.resizable(0, 0)
    LoadScreen.lift()
    LoadScreen.call("wm", "attributes", ".", "-topmost", "1")
    Update()
    def LoadingAnimation():
        while Animation:
            LoadingText = tkinter.Label(LoadScreen, text="Loading.")
            LoadingText.place(relx=.5, rely=.5, anchor="c")
            LoadingText.update()
            time.sleep(2)
            LoadingText = tkinter.Label(LoadScreen, text="Loading..")
            LoadingText.place(relx=.5, rely=.5, anchor="c")
            LoadingText.update()
            time.sleep(2)
            LoadingText = tkinter.Label(LoadScreen, text="Loading...")
            LoadingText.place(relx=.5, rely=.5, anchor="c")
            LoadingText.update()
            time.sleep(2)
    LoadingAnimation()
    LoadScreen.mainloop()

else:
    f.close()
    import os
    path = os.getcwd()
    gpath = path + "/game-version-1.py"
    gnpath = path + "/game-version-1-U.py"
    os.rename(gnpath, gpath)
    os.remove("UpdateIncomplete.txt")


import tkinter
