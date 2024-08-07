import os
import random

# Function to read lines from a file
def read_lines(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Function to write lines to a file
def write_lines(filepath, lines):
    with open(filepath, 'w') as file:
        for line in lines:
            file.write(line + '\n')

# Paths to train and test files
trainfilePath = "train_test_inputs/scared_train_files_with_gt.txt"
testfilePath = "train_test_inputs/scared_test_files_with_gt.txt"

# Read current train and test files
train_files = read_lines(trainfilePath)
test_files = read_lines(testfilePath)

# Determine the number of files to move between train and test sets
num_train_to_val = int(0.2 * len(train_files))
num_val_to_train = int(0.50 * len(test_files))

# Shuffle files to ensure randomness
random.shuffle(train_files)
random.shuffle(test_files)

# Move files from train to val and from val to train
val_files = train_files[:num_train_to_val]
train_files = train_files[num_train_to_val:]
train_files.extend(test_files[:num_val_to_train])
test_files = test_files[num_val_to_train:]

# Write updated train and test files back to disk
write_lines(trainfilePath, train_files)
write_lines(testfilePath, test_files)

print("Dataset re-split done")
