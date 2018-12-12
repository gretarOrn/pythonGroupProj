import pathlib
import showFilter
def download_sort(originPath, destPath):
    path = pathlib.Path(originPath)
    filetypes = ['mp4', 'avi', 'flv', 'wmv', 'mov', 'webm', 'mpeg' ]
    paths = list()
    for x in filetypes:
        paths.extend(path.glob('**/*.'+x))
    ## sort shows and return
    paths = set(map(lambda x: str(x), paths))
    movies = showFilter.show_filter(paths, destPath) 

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
download_sort('downloads', "downloads")