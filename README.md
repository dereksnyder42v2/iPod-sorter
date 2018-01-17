# iPod-sorter

I made this script to organize song files from an old iPod.  The file names were all random 4 letter strings, and songs are contained in folders with equally non-descriptive names, "F00" through "F50" etc.
This script simply creates folders for each letter of the alphabet, and goes through the "Fxx" folders, moving each .m4a song to one of the folders A->Z according to first letter of artist name.

Dependencies:
tinytag library, to get .m4a file metadata - https://pypi.python.org/pypi/tinytag
