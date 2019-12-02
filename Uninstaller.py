###Uninstaller###

import os
import shutil
import tkinter
import time

def Uninstallation():
    path = os.getcwd()
    cfilepath = path + "/Config"
    afilepath = path + "/Assets"

    os.remove("game-version-1.py")
    shutil.rmtree(cfilepath)
    shutil.rmtree(afilepath)
    os.remove("Uninstaller.py")

    ##Kill Tkinter Loading Screen##
    LoadScreen.destroy()

def UninstallationScreen():

    ##Pass Required Global Variables##
    global WindowWidth
    global WindowHeight
    global x
    global y
    global LoadScreen

    ##Kill Tkinter Initial Menu##
    UninstallWindow.destroy()

    ##Setup animation loop variable##
    Animation = True

    ##Create 'Loading' Screen##
    LoadScreen = tkinter.Tk()
    LoadScreen.title("")
    LoadScreen.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, x, y))
    LoadScreen.resizable(0, 0)
    LoadScreen.lift()
    LoadScreen.call("wm", "attributes", ".", "-topmost", "1")
    Uninstallation()
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
UninstallWindow = tkinter.Tk()
WindowWidth = 750
WindowHeight = 500
ScreenWidth = UninstallWindow.winfo_screenwidth()
ScreenHeight = UninstallWindow.winfo_screenheight()
x = (ScreenWidth/2) - (WindowWidth/2)
y = (ScreenHeight/2) - (WindowHeight/2)
UninstallWindow.title("Game Uninstallation Menu")
UninstallWindow.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, x, y))
UninstallWindow.resizable(0, 0)
UninstallWindow.lift()
UninstallWindow.call("wm", "attributes", ".", "-topmost", "1")
ContinueButton = tkinter.Button(UninstallWindow, text="Continue", command=UninstallationScreen, height=1, width=10)
ContinueButton.place(relx=.9, rely=.9, anchor="c")
ExitButton = tkinter.Button(UninstallWindow, text="Exit", command=UninstallWindow.destroy, height=1, width=10)
ExitButton.place(relx=.1, rely=.9, anchor="c")
UninstallWindow.mainloop()
