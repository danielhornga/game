###Game Installer###

##Imports##
import os
import uuid
import subprocess
import sys
import tkinter
import urllib.request
import time

def Installation():

    ##File Path Setup##
    path = os.getcwd()
    cfilepath = path + "/Config"
    afilepath = path + "/Assets"
    gpath = path + "/game-version-1.py"
    upath = path + "/Uninstaller.py"
    os.mkdir(cfilepath)
    os.mkdir(afilepath)

    ##Settings File Creation##
    sfname = os.path.join(cfilepath, "Settings.txt")
    f = open(sfname, "w+")
    f.write("Screen_Height:800\nScreen_Width:800\nFPS:244")
    f.close

    ##Program web downloads##
    url = "https://raw.githubusercontent.com/danielhornga/game/master/game-version-1.py"
    urllib.request.urlretrieve(url, gpath)
    url = "https://raw.githubusercontent.com/danielhornga/game/master/Uninstaller.py"
    urllib.request.urlretrieve(url, upath)

    ##Kill Tkinter Loading Screen##
    LoadScreen.destroy()

def InstallationScreen():

    ##Pass Required Global Variables##
    global WindowWidth
    global WindowHeight
    global x
    global y
    global LoadScreen

    ##Setup animation loop variable##
    Animation = True

    ##Kill Tkinter Initial Menu##
    InstallWindow.destroy()

    ##Create 'Loading' Screen##
    LoadScreen = tkinter.Tk()
    LoadScreen.title("")
    LoadScreen.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, x, y))
    LoadScreen.resizable(0, 0)
    LoadScreen.lift()
    LoadScreen.call("wm", "attributes", ".", "-topmost", "1")
    Installation()
    LoadingText = tkinter.Label(LoadScreen, text="")
    LoadingText.place(relx=.5, rely=.5, anchor="c")
    def LoadingAnimation():
        while Animation:
            LoadingText = tkinter.Label(LoadScreen, text="Loading.")
            LoadingText.update()
            time.sleep(2)
            LoadingText = tkinter.Label(LoadScreen, text="Loading..")
            LoadingText.update()
            time.sleep(2)
            LoadingText = tkinter.Label(LoadScreen, text="Loading...")
            LoadingText.update()
            time.sleep(2)
    LoadingAnimation()
    LoadScreen.mainloop()

##tkinter window initialisation##
InstallWindow = tkinter.Tk()
WindowWidth = 750
WindowHeight = 500
ScreenWidth = InstallWindow.winfo_screenwidth()
ScreenHeight = InstallWindow.winfo_screenheight()
x = (ScreenWidth/2) - (WindowWidth/2)
y = (ScreenHeight/2) - (WindowHeight/2)
InstallWindow.title("Game Installation Menu")
InstallWindow.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, x, y))
InstallWindow.resizable(0, 0)
InstallWindow.lift()
InstallWindow.call("wm", "attributes", ".", "-topmost", "1")
ContinueButton = tkinter.Button(InstallWindow, text="Continue", command=InstallationScreen, height=1, width=10)
ContinueButton.place(relx=.9, rely=.9, anchor="c")
ExitButton = tkinter.Button(InstallWindow, text="Exit", command=InstallWindow.destroy, height=1, width=10)
ExitButton.place(relx=.1, rely=.9, anchor="c")
InstallWindow.mainloop()
