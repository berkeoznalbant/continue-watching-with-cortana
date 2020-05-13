import os, winshell
import sys
from win32com.client import Dispatch
a = winshell.my_documents()

myArg = sys.argv
if len(myArg) > 1:
    showList = ''.join(sys.argv[-1])
else:
    showList = ["Cosmos", "Dynasties", "From The Earth", "Rick And Morty", "Seven Worlds", "The Outsider",
                "The Planets",
                "Westworld"]

folderPath = 'C:/Users/berke/Documents/Shortcuts/'


def createBat(folderPath, show):
    filePath = folderPath + show + '.bat'
    f = open(filePath, 'w')
    f.writelines('nircmd.exe setsysvolume 65535')
    f.writelines('\nnircmd.exe setbrightness 100 1')
    f.writelines('\npy C:/Users/berke/PycharmProjects/cortanaSeries/main.py ' + "\"" + show + "\"")
    # f.writelines('\npy C:/Users/berke/PycharmProjects/cortanaSeries/main.py %s%s%s' %["\"", show, "\""])
    f.close()

    path = os.path.join("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Cortana Commands", show + ".lnk")
    target = r"C:\Users\berke\Documents\Shortcuts/" + show + '.bat'
    wDir = r"C:\Users\berke\Documents\Shortcuts"
    icon = r"C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64/mpc-hc64_nvo.exe"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()


if isinstance(showList, str):
    createBat(folderPath,showList)
else:
    for show in showList:
        createBat(folderPath, show)

