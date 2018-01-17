
'''
f u c k
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
    
    

