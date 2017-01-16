import os

'''
Some sketches have an ID prefixed with 'DU' and others have it prefixed 
with "U". This script renames all the sketches in 'dir' starting with 'DU'
to start with 'U'. e.g. 'DU345.jpg' will be renamed to 'U345.jpg'
'''
dir = 'G:\work\LiLab\DeepEyes\Datasets\d_manatee\sketches'

all_files = os.listdir(dir)

counter = 0
for file in all_files:
    if file.startswith('DU'):
        os.rename(os.path.join(dir, file), os.path.join(dir, file[1:]))
        counter = counter + 1

print "Renamed %d files" % counter        