import pathlib
def download_sort(originPath, destPath):
    path = pathlib.Path(originPath)
    filetypes = ['mp4', 'avi', 'flv', 'wmv', 'mov', 'webm', 'mpeg' ]
    paths = list()
    for x in filetypes:
        paths.extend(path.glob('**/*.'+x))
    ## filter shows
    #movies = showFilter(paths, destPath) 