import pathlib
import re
import os
import shutil
def search_by_season(seasonLis, destPath):
    serieData = []
    showPath = set()
    #showPath2 = set()
    seasonReg = re.compile(r"[Ss]eason[s]*\s*.[0-9]{0,3}|SEASON[S]*\s*.[0-9]{0,3}|season[s]*\s*.[0-9]{0,3}|[Ss]er[íi]a\s*[0-9]{0,3}|([0-9]{0,2}.\s*){0,1}ser[íi]a\s*[0-9]{0,3}|\\\\[Ss]*[0-9]{1,2}\\\\")
    for x in seasonLis:
        serieData.append(x.split('\\')[1:])
    counter = 0
    counter2 = 0
    for x in serieData:
        #þegar bara subfolder inniheldur orðið season
        if len(x) > 1 and re.search(seasonReg, x[1]) is not None and re.search(seasonReg, x[0]) is None:
            counter +=1
            #taka út apostrophies og lowera showname svo title
            season = re.search(seasonReg, x[1]).group()
            seasonF = ''
            showName = x[0].lower()
            #taka út symbols í seríunafni og koma á format sem passar við existing möppur
            showName = re.sub(' - |\(|\)|\'', '', showName)
            showName = re.sub('\.|\,', ' ', showName)
            if season[-1].isdigit() and not season[-2].isdigit(): seasonF += 'Season 0' + season[-1]
            elif season[-1].isdigit() and season[-2].isdigit(): seasonF += 'Season ' + season[-2] + season[-1]
            showPath.add(('/'.join(x) ,destPath+'/'+showName.title()+'/'+seasonF))
            #serieData.remove(x)
            #print(season)
            continue
        #edge case fyrir þátt þar sem parent mappan innihélt 'season + roman numeral ekki digit'
        if len(x) < 2 and re.search(seasonReg, x[0]) is not None:
            counter +=1
            #season = re.split('(\s)E', re.search(seasonReg, x[0]).group())[0]
            season = re.search(seasonReg, x[0]).group()
            showName = x[0].split(season)[0]
            showName = showName.strip()
            if season[-1].isdigit() and not season[-2].isdigit(): season = 'Season 0' + season[-1]
            elif season[-1].isdigit() and season[-2].isdigit(): season = 'Season ' + season[-2] + season[-1]
            showPath.add(('/'.join(x), destPath+'/'+showName.title()+'/'+season))
            #serieData.remove(x)
            #print(season)
            continue
        #þegar bæði parent folder og subfolder innihalda orðið season
        if len(x) > 1 and re.search(seasonReg, x[1]) is not None and re.search(seasonReg, x[0]) is not None:
            counter +=1
            season = re.search(seasonReg, x[1]).group()
            showName = x[0].replace(re.search(seasonReg, x[0]).group(), '')
            #taka út symbols í seríunafni og season og koma á format sem passar við existing möppur
            showName = re.sub(' - |\(|\)|\'', '', showName).lower()
            showName = re.sub('\.|\,', ' ', showName)
            showName = showName.strip()
            if season[-1].isdigit() and not season[-2].isdigit(): season = 'Season 0' + season[-1]
            elif season[-1].isdigit() and season[-2].isdigit(): season = 'Season ' + season[-2] + season[-1]
            showPath.add(('/'.join(x), destPath+'/'+showName.title()+'/'+season))
            #print(season)
            #serieData.remove(x)
            continue
        #Þegar bara parent mappa inniheldur orðið season en enginn subfolder
        if len(x) > 1 and re.search(seasonReg, x[0]) is not None:
            counter +=1
            season = re.search(seasonReg, x[0]).group()
            showName = ''
            reg2 = re.compile(r'[Ss]eason[s]*\s*.*[0-9]{0,3}|SEASON[S]*\s*.*[0-9]{0,3}|season[s]*\s*.*[0-9]{0,3}|[Ss]er[íi]a\s*[0-9]{0,3}|([0-9]{0,2}.\s*){0,1}ser[íi]a\s*[0-9]{0,3}|\\\\[Ss]*[0-9]{1,2}\\\\')
            if re.match(seasonReg, x[0]) is not None:
                continue
            else: showName = re.sub(reg2, '', x[0])
            #edge case fyrir tala + sería(ísl)
            if re.match(r'([0-9]{0,2}.\s*){0,1}ser[íi]a\s*[0-9]{0,3}', season): season = 'Season 0'+season[0]
            #taka út symbols í seríunafni og season og koma á format sem passar við existing möppur
            season = re.sub('\.', ' ', season)
            showName = re.sub(' - |\(|\)|\'', '', showName).lower()
            showName = re.sub('\.|\,', ' ', showName)
            showName = showName.strip()
            #koma season á format: 'Season 01' eða 'Season 12'
            if season[-1].isdigit() and not season[-2].isdigit(): season = 'Season 0' + season[-1]
            elif season[-1].isdigit() and season[-2].isdigit(): season = 'Season ' + season[-2] + season[-1]
            showPath.add(('/'.join(x), destPath+'/'+showName.title()+'/'+season))
            #print(showName.title())
            #serieData.remove(x)
            continue
        #fyrir edge cases þar sem sería heitir bara tölu eða byrjar á tölu
        if re.search(seasonReg, x[0]) is None and re.match('[0-9]{1,2}', x[1]) is not None:
            showName = x[0]
            season = x[1]
            if len(season) > 2 and season[0].isdigit() and season[1].isdigit(): season = 'Season '+ season[0]+season[1]
            elif len(season) > 2 and season[0].isdigit() and not season[1].isdigit(): season = 'Season 0'+ season[0]
            elif len(season) == 1 and season[0].isdigit(): season = 'Season 0'+season[0]
            showPath.add(('/'.join(x), destPath+'/'+showName.title()+'/'+season))
    #búa til dest dir og færa úr upphaflega dir í dest dir
    for x in showPath:
        try:
            os.makedirs(x[1])
        except FileExistsError:
            pass
        try:
            shutil.move('downloads/'+x[0],x[1])
        except:
            pass
        for i in range(1, len(x[0].split('/'))):
            delPath = x[0].split('/')[0:-i]
            #print(delPath)
            try:
                print('downloads/'+'/'.join(delPath))
                os.rmdir('downloads/'+'/'.join(delPath))
            except:
                pass
    #sdata2 = []
    #for x in serieData:
    #    sdata2.append('/'.join(x))

    #print(sdata2)
    #print(counter)
    #for x in serieData:
    #    print(x, '\n')
    #print(counter2)
    #print(showPath - showPath2)
    #print(len(showPath2))
    #print(len(serieData))
    #print(serieData)




#search_by_season(['downloads/Modern Family/Season 21', 'downloads/Breaking Bad/Season 1', 'downloads/Breaking Bad/Season 2', 'downloads/Big Bang Theory/Season.05', 'downloads/RuPaul Season 5'], 'destination')