##Game Patch Number##

patchNumber = float(1.01)

##Check if file "UpdateIncomplete.txt" is present##
try:
    f = open("UpdateIncomplete.txt", "r")
except FileNotFoundError:
    ##Immediately Required Imports##

    import urllib.request
    import os
    import shutil

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
        os.system("game-version-1-U.py 1")
        os.remove("game-version-1.py")

else:
    f.close()
    path = os.getcwd()
    gpath = path + "/game-version-1.py"
    gnpath = path + "/game-version-1-U.py"
    os.rename(gnpath, gpath)
    os.remove("UpdateIncomplete.txt")


print("WORKING")
