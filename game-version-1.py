##Game Patch Number##

patchNumber = float(1.00)

##Immediately Required Imports##

import urllib.request
import os

##Fetch File For Most Recent Patch##

path = os.getcwd()
vLiveFilePath = path + "/Config/Live-Version.txt"
url = "https://raw.githubusercontent.com/danielhornga/game/master/Live-Version"
urllib.request.urlretrieve(url, vLiveFilePath)

##Set Local File Path##
vLocalFilePath = path + "/Config/Local-Version.txt"

##Compare Fetched File To Local File##

f = open(vLiveFilePath, "r")
LiveVersion = float(f.readline())
f.close

f = open(vLocalFilePath, "r")
LiveVersion = float(f.readline())
f.close
