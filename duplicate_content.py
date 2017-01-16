import os
import filecmp

'''
When you're given two directories of sketches, and you wanna combine 
them into one directory, it is possible that some of the sketches are common. 
To avoid duplicates in the final directory, first move all the sketches
from second diectory using windows explorer. The windows explorer will 
move the non-conflictng sketches. Skip the conflicting (same name) sketches.

Now the first directory will have all the sketches, and second directory 
will have the sketches which have same names as the sketches in first directory.

The sketches (in the 2nd directory) with name conflicts should hopefully be
a bit-by-bit same copy of the sketches in the 1st directory. 
But we would like to confirm this !
This script does that.
'''

src_dir = 'G:\work\LiLab\DeepEyes\Datasets\manatee\BatchB_SW DU Sketches'
dst_dir = 'G:\work\LiLab\DeepEyes\Datasets\manatee\BatchA_SW DU Sketches'

dst_files = os.listdir(dst_dir)

# compares the files listed in dst_files in both directories.
# Explanation of cmpfiles() function operation:
#
# If present in both directories:
#   If matches: 
#       append to result[0]
#   else:    
#       append to result[1]
# else (if not present on one or both directories):
#   append to result[2]
result = filecmp.cmpfiles(src_dir, dst_dir, dst_files)

print "Match: ", result[0]
print "Mismatch: ", result[1]
print "Not found:", result[2]