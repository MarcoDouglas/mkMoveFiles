import os
import shutil


def copyFile(origem, dst):
    listWayDst = dst.split('/')

    wayDst = listWayDst.pop(-1)
    if os.path.isdir(wayDst):
        os.mkdir()

    shutil.copy(origem, dst)

def deleteFile(file):
    os.remove(file)

