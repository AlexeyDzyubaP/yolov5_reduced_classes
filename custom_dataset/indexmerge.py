#change indexes -> indexmerge.py 2 1 3 1 4 2 5 2 (first old -> second new and so on)

import os
import sys

directory = "C:\\Users\\Alex\\datasets\\yolo5_coco_pcbtdc\\train"
new_directory = "C:\\Users\\Alex\\datasets\\yolo5_coco_pcbtdc\\new_train"

num_of_merges = (len(sys.argv)-1)//2

print(num_of_merges)


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f, 'r') as file :
            filedata = file.read()
        print(filename)
        lines = filedata.splitlines()
        new_lines = lines
        for i in range(num_of_merges):
            
            for idx, line in enumerate(lines):
                #print(line)
                if line[:1] == sys.argv[i*2+1]:
                    #print(line[:1],idx)
                    #print(line[:1], i, sys.argv[i*2+1])
                    line = sys.argv[i*2+2] + line[1:] # 0 -> 1,2  1 -> 3,4 2 -> 5,6
                    new_lines[idx] = line
                    #filedata[idx] = line
                    #print(line)
                    #print(line[:1], i, sys.argv[i*2+1])

    new_f = os.path.join(new_directory, filename)
    new_filedata = "\n".join(lines)
    with open(new_f, 'w') as file:
            file.write(new_filedata)
    #print(filedata)
    #print(file)

        
