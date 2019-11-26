###Game Installer###

import os
import uuid
import subprocess
import sys
import tkinter
import urllib.request

##tkinter window initialisation

subprocess.call([sys.executable, "-m", "pip", "install", "arcade"])

path = os.getcwd()
cfilepath = path + "/Config"
afilepath = path + "/Assets"
gpath = path + "/game-version-1.py"
upath = path + "/Uninstaller.py"
os.mkdir(cfilepath)
os.mkdir(afilepath)

sfname = os.path.join(cfilepath, "Settings.txt")
f = open(sfname, "w+")
f.write("Screen_Height:800\nScreen_Width:800\nFPS:244")
f.close

url = 'https://raw.githubusercontent.com/danielhornga/game/master/game-version-1.py'
urllib.request.urlretrieve(url, gpath)

url = 'https://raw.githubusercontent.com/danielhornga/game/master/Uninstaller.py'
urllib.request.urlretrieve(url, upath)

