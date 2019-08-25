'''
Write a simple script to demonstrate your understanding of lists 
'''
#getting a directory listing

import os
import os.path
import glob

pyfiles = glob.glob('*.py')

#get file sizes and modification dates
name_size_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                  for name in pyfiles]

for name, size, mtime in name_size_date:
    print(name, size, mtime)
    
#Another way: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.ST_SIZE, meta.ST_MTIME)