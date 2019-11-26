###Uninstaller###

import os
import shutil

path = os.getcwd()
cfilepath = path + "/Config"
afilepath = path + "/Assets"

os.remove("ALPHAv1.py")
shutil.rmtree(cfilepath)
shutil.rmtree(afilepath)
os.remove("Uninstaller.py")