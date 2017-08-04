#!/usr/bin/env python
from sys import argv

def parse(file):
    ret = []
    with open(file) as f:
        for line in f:
            ret.append(int(line))
    return ret

def mergeAndCount(left, right, count):
    ret = []
    leftIndex = 0
    rightIndex = 0
    while (leftIndex < len(left) or rightIndex < len(right)):
        if leftIndex == len(left):
            ret.append(right[rightIndex])
            rightIndex += 1
        elif rightIndex == len(right):
            ret.append(left[leftIndex])
            leftIndex += 1
        elif right[rightIndex] < left[leftIndex]:
            ret.append(right[rightIndex])
            rightIndex += 1
            count[0] += len(left) - leftIndex
        else:
            ret.append(left[leftIndex])
            leftIndex += 1
    return ret

def countInversions(numbers, count):
    if (len(numbers) == 1 or len(numbers) == 0):
        return numbers
    mid = len(numbers) / 2
    left = countInversions(numbers[:mid], count)
    right = countInversions(numbers[mid:], count)
    merged = mergeAndCount(left, right, count)
    return merged

if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: ./count-inversions.py newline-separated-list")
        print("where list contains all  numbers 1 through N without repeats")
        exit()
    count = [0]
    print("Sorted array: " + str(countInversions(parse(argv[1]), count)))
    print("Inversion count: " + str(count[0]))
