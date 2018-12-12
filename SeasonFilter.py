import pathlib
import re
import os
import shutil
def search_by_season(seasonLis, destPath):
    serieData = []
    showPath = []
    for x in seasonLis:
        serieData.append(x.split('/')[1:])
    for x in serieData:
        if re.search('[Ss]eason|[Ss][0-9]{1,2}', x[-1]) is not None and re.search('[Ss]eason', x[0]) is None:
            season = 'Season 0' + x[1][-1]
            showPath.append(destPath+'/'+x[0].title()+'/'+season)
        if len(x) < 2:
            print(x)
    print(showPath)

search_by_season(['downloads/Modern Family/Season 2', 'downloads/Breaking Bad/Season 1', 'downloads/Breaking Bad/Season 2', 'downloads/Big Bang Theory/Season.05', 'downloads/RuPaul Season 5'], 'destination')