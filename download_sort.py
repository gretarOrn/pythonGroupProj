import pathlib
import showFilter
import os
def download_sort(originPath, destPath):
    path = pathlib.Path(originPath)
    paths = list()
    filetypes = ['idx', 'sfv', 'srt','mp4', 'avi', 'flv', 'wmv', 'mov', 'webm', 'mpeg','mkv' ]
    delfiletypes = ['txt', 'rar', 'zip', 'nfo', 'jpg', 'jpeg', 'dat', 'stf', 'part', 'mta','png']
    for x in range(0,50):
        if x < 10: delfiletypes.append('r0'+str(x))
        delfiletypes.append('r'+str(x))
    for x in delfiletypes:
        paths.extend(path.glob('**/*.'+x))
    for x in paths:
        try:
            os.remove(x)
        except:
            pass
    paths = list()
    for x in filetypes:
        paths.extend(path.glob('**/*.'+x))
    #print(len(paths))
    ## sort shows and return
    paths = set(map(lambda x: str(x), paths))
    movies = showFilter.show_filter(paths, destPath) 
    paths = list()
    for x in filetypes:
        paths.extend(path.glob('**/*.'+x))
    paths = set(map(lambda x: str(x), paths))
    #print(len(paths))
    #print('\n'.join(paths))
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
    
download_sort('downloads', "destination")