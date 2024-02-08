def isBadVersion(i):
    return i == 0

def firstBad(inputArray):
    for i in range(len(inputArray)):
        if isBadVersion(inputArray[i]):
            return i

inputArray = [1, 2, 2, 0, 4, 5, 0, 6, 7, 8, 9] #in this scenrio, 0 is a bad case
print(f"this is the first bad index: {firstBad(inputArray)}")