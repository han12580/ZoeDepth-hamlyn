import os
import random

import numpy as np
from PIL import Image

basedir = "data/nyu/scared"
limit_rate=0.05
### data/nyu/scared/dataset_{i}/keyframe_{i}/data/left/000000.png

allFields = []
for dataset in os.listdir(basedir):
    dataset_dir = basedir+"/"+dataset+""
    for frame in os.listdir(dataset_dir):
        frame_dir = dataset_dir+"/"+frame+"/data/left/"
        depth_dir = dataset_dir+"/"+frame+"/data/depthmap/"
        for depthpath in os.listdir(depth_dir):
            depth_path=depth_dir+"/"+depthpath
            imgpath=frame_dir+"/"+depthpath
            depth=Image.open(depth_path)
            depth=np.array(depth)
            size=depth[depth!=0].size
            if(size<depth.size*limit_rate):
                print(depth_dir,depthpath, "is empty")
                continue
            line=imgpath[8:]+" "+depth_path[8:]+" 1035.308"
            allFields.append(line)
random.shuffle(allFields)
tranSplit = int(len(allFields)*0.8)
##random
tranFiles =allFields[:tranSplit]
testFiles =allFields[tranSplit:]
trainfilePath="train_test_inputs/scared_train_files_with_gt.txt"
with open(trainfilePath,"w") as f:
    for tranFile in tranFiles:
        f.write(tranFile+"\n")
    f.close()
testfilePath="train_test_inputs/scared_test_files_with_gt.txt"
with open(testfilePath,"w") as f:
    for testFile in testFiles:
        f.write(testFile+"\n")
    f.close()

print("dataset process done")


