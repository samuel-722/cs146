
def matchTarget(nums, target):
    num_indeces = {} #create a dictionary

    for i, num in enumerate(nums): #iterate through array along with its indice
        match = target - num #calculate the match of each number that would get it to its target
        if match in num_indeces: #check if match is in the dictionary
            return [num_indeces[match], i] #if found, return index of the both numbers
        num_indeces[num] = i
    return[] #return nothing (an empty list) if nothing is found

nums = [0,1,2,3,4,5,6,7,8,9]
target = 17
print(matchTarget(nums, target))