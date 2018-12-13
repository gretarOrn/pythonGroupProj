import pathlib
import re
import os
import shutil
def search_by_season(seasonLis, destPath):
    serieData = []
    showPath = set()
    tmp = set()
    seasonReg = re.compile("[Ss](eason)[s]*\s*.*[0-9]{0,3}|(SEASON)[S]*\s*.*[0-9]{0,3}|(season)[s]*\s*.*[0-9]{0,3}|[Ss](er)[íi](a)\s*.*[0-9]{0,3}|\\\\[Ss]*[0-9]{1,2}\\\\")
    for x in seasonLis:
        serieData.append(x.split('\\')[1:])
    counter = 0
    for x in serieData:
        if len(x) > 1 and re.search(seasonReg, x[1]) is not None and re.search(seasonReg, x[0]) is None:
            counter +=1
            #taka út apostrophies og lowera showname svo title
            season = re.search(seasonReg, x[1]).group()
            seasonF = ''
            showName = x[0].lower()
            showName = re.sub(' - |\(|\)|\'', '', showName)
            showName = re.sub('\.', ' ', showName)
            if season[-1].isdigit() and not season[-2].isdigit(): seasonF += 'Season 0' + season[-1]
            elif season[-1].isdigit() and season[-2].isdigit(): seasonF += 'Season ' + season[-2] + season[-1]
            showPath.add(('/'.join(x) ,destPath+'/'+showName.title()+'/'+seasonF))
            serieData.remove(x)
            continue
        if len(x) < 2 and re.search(seasonReg, x[0]) is not None:
            counter +=1
            season = re.split('(\s)E', re.search(seasonReg, x[0]).group())[0]
            showName = x[0].split(season)[0]
            showName = showName.strip()
            showPath.add(('/'.join(x), destPath+'/'+showName.title()+'/'+season))
            serieData.remove(x)
            continue
        if len(x) > 1 and re.search(seasonReg, x[1]) is not None and re.search(seasonReg, x[0]) is not None:
            counter +=1
            season = re.search(seasonReg, x[1]).group()
            showName = x[0].replace(re.search(seasonReg, x[0]).group(), '')
            showName = re.sub(' - |\(|\)|\'', '', showName).lower()
            showName = re.sub('\.', ' ', showName)
            showName = showName.strip()
            showPath.add(('/'.join(x), destPath+'/'+showName.title()+'/'+season))
            serieData.remove(x)
            continue

        if len(x) > 1 and re.search(seasonReg, x[0]) is not None:
            counter +=1
            #sReg2 = re.compile("[Ss](eason)[s]*\s*.*[0-9]{0,3}|(SEASON)[S]*\s*.*[0-9]{0,3}|(season)[s]*\s*.*[0-9]{0,3}|[Ss](er)[íi](a)\s*.*[0-9]{0,3}|\\\\[Ss]*[0-9]{1,2}\\\\")
            season = re.search(seasonReg, x[0]).group()
            showName = ''
            if re.match(seasonReg, x[0]) is not None:
                continue
            else: showName = x[0].replace(season, '')
            showName = re.sub(' - |\(|\)|\'', '', showName).lower()
            showName = re.sub('\.', ' ', showName)
            showName = showName.strip()
            #print(showName+'/'+season)
            showPath.add(('/'.join(x), destPath+'/'+showName.title()+'/'+season))
            serieData.remove(x)
            continue
    #print(showPath)
    for x in showPath:
        try:
            os.makedirs(x[1])
        except FileExistsError:
            pass
        try:
            shutil.move('downloads/'+x[0],x[1])
        except:
            pass
    #print(showPath)
    #print(counter)
    #print(len(seasonLis))


#search_by_season(['downloads/Modern Family/Season 21', 'downloads/Breaking Bad/Season 1', 'downloads/Breaking Bad/Season 2', 'downloads/Big Bang Theory/Season.05', 'downloads/RuPaul Season 5'], 'destination')