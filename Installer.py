###Game Installer###

##Imports##
import os
import uuid
import subprocess
import sys
import tkinter
import urllib.request
import time
import winshell
from win32com.client import Dispatch

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

    ##Keybindings File Creation
    kfname = os.path.join(cfilepath, "Keybindings.txt")
    f = open(kfname, "w+")
    f.close()
    
    ##Program web downloads##
    url = "https://raw.githubusercontent.com/danielhornga/game/master/game-version-1.py"
    urllib.request.urlretrieve(url, gpath)
    url = "https://raw.githubusercontent.com/danielhornga/game/master/Uninstaller.py"
    urllib.request.urlretrieve(url, upath)

    ##Shortcut creation##
    desktop = winshell.desktop()
    dpath = desktop + "/GAME_VERSION_1.lnk"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(dpath)
    shortcut.Targetpath = gpath
    shortcut.WorkingDirectory = path
    shortcut.IconLocation = gpath
    shortcut.save()

    ##Kill Tkinter Loading Screen##
    LoadScreen.destroy()

def InstallationScreen():

    ##Pass Required Global Variables##
    global WindowWidth
    global WindowHeight
    global x
    global y
    global LoadScreen

    ##Kill Tkinter Initial Menu##
    InstallWindow.destroy()

    ##Setup animation loop variable##
    Animation = True

    ##Create 'Loading' Screen##
    LoadScreen = tkinter.Tk()
    LoadScreen.title("")
    LoadScreen.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, x, y))
    LoadScreen.resizable(0, 0)
    LoadScreen.lift()
    LoadScreen.call("wm", "attributes", ".", "-topmost", "1")
    Installation()
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
BaseText = tkinter.Label(InstallWindow, text="Line 1 Test") #Title Text ~TO MAKE BOLD
BaseText.place(relx=.5, rely=.2, anchor="c")
BaseText = tkinter.Label(InstallWindow, text="Line 2 Test") #Main Text Body
BaseText.place(relx=.5, rely=.3, anchor="c")
BaseText = tkinter.Label(InstallWindow, text="Line 3 Test") # ""
BaseText.place(relx=.5, rely=.4, anchor="c")
BaseText = tkinter.Label(InstallWindow, text="Line 4 Test") # ""
BaseText.place(relx=.5, rely=.5, anchor="c")
BaseText = tkinter.Label(InstallWindow, text="Line 5 Test") # ""
BaseText.place(relx=.5, rely=.6, anchor="c")
BaseText = tkinter.Label(InstallWindow, text="Line 6 Test") #Last line to leave spacing of at least .2 
BaseText.place(relx=.5, rely=.7, anchor="c")
ContinueButton = tkinter.Button(InstallWindow, text="Continue", command=InstallationScreen, height=1, width=10)
ContinueButton.place(relx=.9, rely=.9, anchor="c")
ExitButton = tkinter.Button(InstallWindow, text="Exit", command=InstallWindow.destroy, height=1, width=10)
ExitButton.place(relx=.1, rely=.9, anchor="c")
InstallWindow.mainloop()
