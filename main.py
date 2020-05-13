import os
import subprocess
from pynput.keyboard import Key, Controller
import time
import winreg
import re
import glob
from moviepy.video.io.VideoFileClip import VideoFileClip
import sys

foundInReg = False
isWatched = False
isLastEpisode = False
fullPath = None
lastPosDuration = None
folderName = None
showFound = None

myArg = sys.argv
if len(myArg) > 1:
    showName = ''.join(sys.argv[-1])
else:
    showName = "Seinfeld"

textPath = "C:/Users/berke/Documents/Shortcuts/%s.txt" % showName
foundInTextFile = os.path.isfile(showName + ".txt")

for show in os.listdir("E:/Diziler"):
    if re.search(showName, show, re.IGNORECASE):
        folderName = show
        showFound = True
        break

showFolderPath = "E:/Diziler/%s/" % folderName
currEpInd = -1
# episodeList = glob.glob([showFolderPath + "**/*.mkv", showFolderPath + "**/*.mp4"], recursive=True)
episodeList = [item for sublist in [glob.glob(showFolderPath + ext, recursive=True) for ext in ["**/*.mp4", "**/*.mkv"]] for item in sublist]

registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\MPC-HC\MPC-HC\Settings", 0,
                              winreg.KEY_READ)

for i in range(40):
    value, regtype = winreg.QueryValueEx(registry_key, "File Name " + str(i))
    if re.search(showName, value, re.IGNORECASE):
        foundInReg = True
        fullPath = value
        # currID = ''.join(re.findall("S\d\dE\d\d",fullPath))
        winreg.CloseKey(registry_key)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\MPC-HC\MPC-HC\Settings", 0,
                                      winreg.KEY_READ)
        lastPosDuration, regtype = winreg.QueryValueEx(registry_key, "File Position " + str(i))
        lastPosDuration = float(lastPosDuration) / 10000000
        break

if foundInReg:
    fileName = fullPath.split("\\")[-1]
    for episode in episodeList:
        currEpInd += 1
        if fileName in episode:
            episodeDur = VideoFileClip(fullPath).duration
            isLastEpisode = currEpInd + 1 >= len(episodeList)
            isWatched = lastPosDuration / episodeDur > 0.9 or lastPosDuration == 0
            break
    if isWatched and not isLastEpisode:
        currEpInd += 1
elif foundInTextFile:
    f = open(textPath, 'r')
    preEpInd = int(f.read())
    f.close()
    currEpInd = preEpInd + 1
else:
    currEpInd = 0

currEpPath = episodeList[currEpInd]
# myCommand ="\"%s\" %s" % (, "/fullscreen")
# fullCommand = '\"C:/Program Files (x86)/K-Lite Codec Pack/MPC-HC64/mpc-hc64_nvo.exe\" ' + myCommand
# os.system(fullCommand)
subprocess.Popen(["C:/Program Files (x86)/K-Lite Codec Pack/MPC-HC64/mpc-hc64_nvo.exe", currEpPath])

f = open(textPath, 'w')
f.write(str(currEpInd))
f.close()

time.sleep(2)
Controller().press('f')
Controller().release('f')
