import pathlib
import re
import os
import shutil
def deleter(path):
    filetypes = ['srt','mp4', 'avi', 'flv', 'wmv', 'mov', 'webm', 'mpeg','mkv' ]
    path = pathlib.Path(path)
    paths = list()
    for x in filetypes:
        paths.extend(path.glob('**/*.'+x))
    if len(paths) == 0:
        shutil.rmtree(path)
    return
def mapping_func(fileName):
    if re.search(r'^[Ss]([0-9]+)[eE][0-9]+[\.\-\s]*(.*)', fileName.split('\\')[-1]) != None:
        tempTuple = re.search(r'^[Ss]([0-9]+)[eE][0-9]+[\.\-\s]*(.*)', fileName.split('\\')[-1]).groups()
        return (fileName, (tempTuple[1].split(' - ')[0], tempTuple[0]))
    elif re.search(r'^(.*)[\.\-\s]*[Ss]([0-9]+)[\.\-\s]*[eE][\.\-\s]*[0-9]+', fileName.split('\\')[-1]) != None:
        return (fileName, re.search(r'^(.*)[\.\-\s]*[Ss]([0-9]+)[\.\-\s]*[eE][\.\-\s]*[0-9]+', fileName.split('\\')[-1]).groups())
    elif re.search(r'^(.*)[\s\[\-\_\.]+([0-9]{1,2})\s*[xX]\s*[0-9]+', fileName.split('\\')[-1]) != None:
        return (fileName, re.search(r'^(.*)[\s\[\-\_\.]+([0-9]{1,2})\s*[xX]\s*[0-9]+', fileName.split('\\')[-1]).groups())
    elif re.search(r'^(.*)[\.\-\s]*([0-9]{1,2})[0-9]{2}\.*', fileName.split('\\')[-1]) != None:
        return (fileName,re.search(r'^(.*)[\.\-\s]*([0-9]{1,2})[0-9]{2}\.*', fileName.split('\\')[-1]).groups())
    else:
        print("couldnt match: "+fileName.split('\\')[-1]+"\n")
        return None
def single_show_filter(paths, destPath):
    #filenames = set(map(lambda x : x.split('\\')[-1], paths))
    #print('\n'.join(filenames))
    typeReg = "Avi|Mp4|Flv|Wmv|Mov|Webm|Mpeg"
    filetypes = ['srt','mp4', 'avi', 'flv', 'wmv', 'mov', 'webm', 'mpeg','mkv' ]
    #filetypes = ['nfo', 'jpg', 'jpeg', 'png', 'txt', 'sfv', 'rar', 'zip']
    info = list(map(mapping_func,paths))
    for x in info:
        if x == None:
            continue
        if "sample" in x[1][0].lower():
            try:
                os.remove(x[0])
            except:
                pass
            try:
                os.removedirs('/'.join(newPath.split('\\')[0:-1]))
            except:
                pass
            continue
        if len(x[1][1]) < 2:
            season = "Season 0" + x[1][1]
        else :
            season = "Season " + x[1][1]
        showName = (' '.join(re.findall(r"[A-Za-z0-9aáðþéúíæóýö]+",x[1][0])).title()).strip()
        showName = str(re.sub(typeReg,'',showName)).strip()
        #print(showName)
        newPath = destPath+'/'+showName+'/'+season
        #print(x)
        if os.path.exists(x[0]):
            try:
                os.makedirs(newPath)
            except FileExistsError:
                pass
        
        try:
            shutil.move(x[0],newPath)
        except:
            pass
        for i in range(1, len(x[0].split('/'))):
            delPath = x[0].split('/')[0:-i]
            try:
                os.rmdir(delPath)
            except:
                pass
        #deleter(parent)
        #print('/'.join(x[0].split('\\')[0:-1]))
        #recursive_del(x[0])
        #try:
        #    os.removedirs('/'.join(newPath.split('\\')[0:-1]))
        #except:
        #    pass

        
    #print(len(filenames))

    #for i in paths:
    #    fileName = filename.append(str(i).split('\\')[-1])
    #info = list(re.search('^(.*)\.s([0-9]+)e[0-9]+', fileName).groups())
    #season = "Season "+info[1]
    #showName = ' '.join(info[0].split('.')).title()
    #showPath = destDir+'/'+showName+'/'+season
    #try:
    #    os.makedirs(showPath)
    #except FileExistsError:
    #    print(showName)
    #shutil.move(str(paths[0]),showPath)
    ## DELETE'A source möppu
    #print(showPath) 
    #print(season)
    #print(len(paths))
