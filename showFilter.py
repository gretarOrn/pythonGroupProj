import pathlib
import re
import SeasonFilter
def show_filter(paths, destPath):
    
    seasonReg = re.compile("[Ss](eason)[s]*\s*.*[0-9]{0,3}|(SEASON)[S]*\s*.*[0-9]{0,3}|(season)[s]*\s*.*[0-9]{0,3}|[Ss](er)[íi](a)\s*.*[0-9]{0,3}|\\\\[Ss]*[0-9]{1,2}\\\\")
    singleShowReg = re.compile("[sS][0-9]{1,2}\s*[eE][0-9]{1,2}|[0-9]{1,2}[xX][0-9]{1,2}")
    movieReg = re.compile("(19)[0-9]{2}|(20)[01][0-8]")
    # reg fyrir season möppur
    # reg fyrir staka þætti season
    Seasons = set(filter(seasonReg.search,paths))
    paths = paths - Seasons
    SeasonFilter.search_by_season(Seasons, destPath)
    Episodes = set(filter(singleShowReg.search,paths))
    paths = paths - Episodes
    movies = set(filter(movieReg.search,paths))
    paths = paths - movies
    paths = list(paths)
    paths.sort()
    #print('\n'.join(Seasons))
    #print('\n'.join(paths))
    #print(len(paths))
    #for i in paths:
    #    if i.split('/')[-2] == season:
    #print("bla")
    return movies