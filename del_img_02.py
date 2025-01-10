txtfile=r"D:\otherPj\ZoeDepth-hamlyn\train_test_inputs\hamlyn_train_files_with_gt.txt"
all_lines=[]
with open(txtfile,"r") as f:
    lines=f.readlines()
    for line in lines:
        if line.__contains__("image02"):
            continue
        all_lines.append(line)
with open("test.txt","w") as f:
    for tranFile in all_lines:
        f.write(tranFile)
    f.close()
