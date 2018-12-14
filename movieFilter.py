import pathlib
import re
import os
import shutil
def movie_filter(paths, destPath):
    #counter = 0
    #try:
    #    os.makedirs(destPath+'/Movies/')
    #except FileExistsError:
    #    pass
    for x in paths:
        if "sample" in x.lower():
            try:
                os.remove(x)
            except:
                pass
        newPath = destPath+'/Movies/'+'/'.join(x.split('\\')[1:-1])
        #print(newPath)
        try:
            os.makedirs(newPath)
        except FileExistsError:
            pass
        try:
            shutil.move(x,newPath)
            counter+=1
        except:
            pass
    #print('\n'.join(paths))
    #print(len(paths))