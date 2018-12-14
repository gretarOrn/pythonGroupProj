import pathlib
import re
import singleShowFilter
import SeasonFilter
import movieFilter
def show_filter(paths, destPath):
    
    seasonReg = re.compile(r"[Ss](eason)[s]*\s*.*[0-9]{0,3}|(SEASON)[S]*\s*.*[0-9]{0,3}|(season)[s]*\s*.*[0-9]{0,3}|[Ss](er)[íi](a)\s*.*[0-9]{0,3}|\\\\[Ss]*[0-9]{1,2}\\\\|[Ss](erie)s*|\\\\\d{1,2}\\\\")
    singleShowReg = re.compile(r"[sS][0-9]{1,2}\s*[eE][0-9]{1,2}|\D+[0-9]{1,2}[xX][0-9]{1,2}\D+")
    secondSingleShowReg = re.compile(r"[\.\-\_\s][0-9]{3}[\.\-\_\s]")
    movieReg = re.compile(r"(19)[0-9]{2}|(20)[01][0-8]")
    # reg fyrir season möppur
    # reg fyrir staka þætti season
    Seasons = set(filter(seasonReg.search,paths))
    paths = paths - Seasons
    SeasonFilter.search_by_season(Seasons, destPath)
    Episodes = set(filter(singleShowReg.search,paths))
    singleShowFilter.single_show_filter(Episodes,destPath)
    paths = paths - Episodes
    movies = set(filter(movieReg.search,paths))
    movieFilter.movie_filter(movies,destPath)
    paths = paths - movies
    Episodes2 = set(filter(secondSingleShowReg.search, paths))
    singleShowFilter.single_show_filter(Episodes2,destPath)
    paths = list(paths)
    paths.sort()
    #print('\n'.join(Seasons))
    #print('\n'.join(paths))
    #print(paths)
    #for i in paths:
    #    if i.split('/')[-2] == season:
    #print("bla")
    return movies