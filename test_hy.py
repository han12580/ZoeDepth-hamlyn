import os
import random

import numpy as np
from PIL import Image

basedir = "/home/han/han/hy"

### hy/dataset/
#              image01
#              image02
#              depth01
#              depth02

allFields = []
for dataset in os.listdir(basedir):
    dataset_dir = basedir+"/"+dataset+""
    frame01_dir = dataset_dir+"/image01"
    frame01depth_dir = dataset_dir+"/depth01"
    frame02_dir = dataset_dir+"/image02"
    frame02depth_dir = dataset_dir+"/depth02"
    for image_name in os.listdir(frame01_dir):
        image_path = frame01_dir+"/"+image_name
        depth_path = frame01depth_dir+"/"+image_name.replace("jpg","png")
        line=image_path[14:]+" "+depth_path[14:]+" 1035.308"
        allFields.append(line)
    for image_name in os.listdir(frame02_dir):
        image_path = frame01_dir+"/"+image_name
        depth_path = frame01_dir+"/"+image_name.replace("image","depth")
        line=image_path[14:]+" "+depth_path[14:]+" 1035.308"
        allFields.append(line)
random.shuffle(allFields)
tranSplit = int(len(allFields)*0.8)
##random
tranFiles =allFields[:tranSplit]
testFiles =allFields[tranSplit:]
trainfilePath="train_test_inputs/hamlyn_train_files_with_gt.txt"
with open(trainfilePath,"w") as f:
    for tranFile in tranFiles:
        f.write(tranFile+"\n")
    f.close()
testfilePath="train_test_inputs/hamlyn_test_files_with_gt.txt"
with open(testfilePath,"w") as f:
    for testFile in testFiles:
        f.write(testFile+"\n")
    f.close()

print("dataset process done")


