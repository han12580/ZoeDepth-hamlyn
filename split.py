import os
import random
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Personal information')

    parser.add_argument('--test_id', type=int, help='Name of the test 0-9')
    return parser.parse_args()
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

def split(test_id = 0):
    # Paths to train and test files
    trainfilePath = "train_test_inputs/scared_train_files_with_gt.txt"
    testfilePath = "train_test_inputs/scared_test_files_with_gt.txt"
    allfilePath = "train_test_inputs/scared_all_files_with_gt.txt"
    # Read all files
    all_files = read_lines(allfilePath)
    # split 10 parts and set test_id as test set
    num_files = len(all_files)
    num_test_files = int(num_files/10)
    train_files = all_files[:num_test_files*test_id] + all_files[num_test_files*(test_id+1):]
    test_files = all_files[num_test_files*test_id:num_test_files*(test_id+1)]

    # Write updated train and test files back to disk
    write_lines(trainfilePath, train_files)
    write_lines(testfilePath, test_files)

    print("Dataset re-split done")

if __name__ == "__main__":
    args = parse_args()
    split(args.test_id)