import os

'''
Some sketches have an ID prefixed with 'DU' and others have it
prefixed with "U". This script check if in a given directory 'dir'
Check if a DU file has same ID (number) as a U file
'''

dir = 'G:\work\LiLab\DeepEyes\Datasets\d_manatee\SW DU Sketches'

all_files = os.listdir(dir)

files = []        
# Search for duplicate ID across all (irrespective of prefix or file extension)
for file in all_files:
    if file.startswith('DU'):
        files.append(file[2:].split('.')[0])
    elif file.startswith('U'):
        files.append(file[1:].split('.')[0])
    else:
        print 'Weird file name: ', file

seen = set()
for id in files:
    if id not in seen:
        seen.add(id)    
    else:
        print "Duplicate found ID: ", id











