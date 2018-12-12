import pathlib
import re
import os
import shutil
def search_by_season(seasonLis, destPath):
    serieData = []
    showPath = set()
    seasonReg = re.compile("[Ss](eason)[s]*\s*.*[0-9]{0,3}|(SEASON)[S]*\s*.*[0-9]{0,3}|(season)[s]*\s*.*[0-9]{0,3}|[Ss](er)[íi](a)\s*.*[0-9]{0,3}|\\\\[Ss]*[0-9]{1,2}\\\\")
    for x in seasonLis:
        serieData.append(x.split('\\')[1:])
    for x in serieData:
        if len(x)>1 and re.search(seasonReg, x[1]) is not None and re.search(seasonReg, x[0]) is None:
            season = re.search(seasonReg, x[1]).group()
           # print(season)
            seasonF = ''
            if season[-1].isdigit() and not season[-2].isdigit(): seasonF += 'Season 0' + season[-1]
            elif season[-1].isdigit() and season[-2].isdigit(): seasonF += 'Season ' + season[-2] + season[-1]
            showPath.add(destPath+'/'+x[0].title()+'/'+seasonF)
    print('\n'.join(showPath))
    print(len(showPath))
    print(len(seasonLis))


#search_by_season(['downloads/Modern Family/Season 21', 'downloads/Breaking Bad/Season 1', 'downloads/Breaking Bad/Season 2', 'downloads/Big Bang Theory/Season.05', 'downloads/RuPaul Season 5'], 'destination')