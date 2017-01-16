from __future__ import print_function

import os
import shutil

import random
seed = 1337 # For reproduciility

'''
Divideds the dataset (sketches) into three parts: train, val, test
Creates three directories for training, validation and test set
'''

#division of entire dataset. Must sum to 100%
div = {'train': 60, 'val': 20, 'test': 20}
dir = 'path/to/dataset/directory'

# the source_dir could be same as any one the other directories
source_dir = os.path.join(dir, 'sketches')
train_dir  = os.path.join(dir, 'sketches_train')
val_dir    = os.path.join(dir, 'sketches_test')
test_dir   = os.path.join(dir, 'sketches_val')

# Test if directory paths are correct
dirs = [source_dir, train_dir, val_dir, test_dir]
if not os.path.exists(source_dir):
    print('Source directory {0:s} does not exist.'.format(source_dir))
    exit(0)
        
for dir in dirs[1:]:
    if not os.path.exists(dir):
        os.mkdir(dir)

# Sanity check
sum = 0        
for value in div.itervalues():
    sum += value
if sum is not 100:
    print('The entries in "div" must sum to 100. Current sum:{0:d}'.format(sum))
    exit(0)
    
# get a list of all sketches
files = os.listdir(source_dir)
weird_files = []
for file in files:
    if file.lower().endswith('.jpg') or file.lower().endswith('.tif'):
        pass
    else:
        weird_files.append(file)

if weird_files:
    print('Source directory contains weird files: ', weird_files,
        'eliminate them and rerun. Aborting for now.')
    exit(0)
else:
    sketches = os.listdir(source_dir)
    if not len(sketches): # Sanity check
        print('No sketches found in source directory. Aborting')
        exit(0)
    
# Shuffle sketches
random.Random(seed).shuffle(sketches)    

# Compute division indices
num_samples = len(sketches)
train_val_idx = (div['train'] * num_samples)/100
val_test_idx = train_val_idx + (div['val'] * num_samples)/100

sketchs_train = sketches[:train_val_idx]
sketches_val = sketches[train_val_idx:val_test_idx]
sketches_test = sketches[val_test_idx:]
sketch_distribution = [sketchs_train, sketches_val, sketches_test]

print('Found {0:d} sketches.'.format(num_samples))
print('Distribution Traning: {0:d}, Validation: {1:d}, Testing:{2:d}'.format(\
    len(sketchs_train), len(sketches_val), len(sketches_test)))
print('Now performing shuffling ... ')
#print(sketch_distribution); exit(0)

# Perform file movements
for i in range(3):
    destination_dir = dirs[i + 1]
    for sketch in sketch_distribution[i]:
        shutil.move(os.path.join(source_dir, sketch), destination_dir)  # Move the file
        #shutil.copy(os.path.join(source_dir, sketch), destination_dir) # Copy the file
print('Done')


















