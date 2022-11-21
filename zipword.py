import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)
global result
result = 0
global tried
tried = 0
c=0
if not zipf:
    print('the zipped file is not password protected. You can successfully open it')