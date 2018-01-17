'''
Removes all empty folders under <root>

Derek Snyder
'''

import os

root="c:\\users\\derek\\music"

os.chdir(root)
for subfolder in os.listdir(os.getcwd()):
    if '*' in subfolder or '/' in subfolder or not os.path.isdir(subfolder) or '.ini' in subfolder:
        continue
    thisFolder = root+'\\'+subfolder
    #print thisFolder
    if os.listdir(thisFolder) == []:
        print thisFolder
        os.rmdir(thisFolder)
    
