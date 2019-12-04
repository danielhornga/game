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

##Compare Fetched File To Local Patch Number##

f = open(vLiveFilePath, "r")
LiveVersion = float(f.readline())
f.close

if LiveVersion != patchNumber:
  ##Code to update here

else:
  ##Game Code here##
