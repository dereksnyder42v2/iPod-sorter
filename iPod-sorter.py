
'''
Script to alphabetize randomly named songs, off an old iPod.
For some reason filenames on the iPod (the one I tested anyways, ~2010 nano)
were just random 4 letter strings, but artist/ album/ other metadata was
still present. And then they were further jumbled by placing files in folders 
"F00" through "F50" and so on. So this script goes through those folders,
and moves files to different directories labeled A-Z

Derek Snyder
1/18/2018

'''

import os, tinytag, shutil

alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']
foldersToSort = list()
root = 'c:\\users\\derek\\music'
os.chdir(root)

for subfolder in os.listdir(os.getcwd()):
    if os.path.isdir(subfolder) and subfolder not in alphabet:
        foldersToSort.append(subfolder)

#make a folder for every letter, to alphabetize songs by artist
for letter in alphabet:
    try:
        os.mkdir(letter)
    except WindowsError:
        break

print foldersToSort

for folder in foldersToSort:
    os.chdir(root + '\\' + folder)
    for songfile in os.listdir(os.getcwd()):
        song = tinytag.TinyTag.get(songfile)
        if song.artist != None:
            shutil.move(songfile, root+'\\'+song.artist[0].upper() )
        else:
            pass
    os.chdir(root)
    
    

