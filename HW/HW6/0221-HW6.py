from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    result = [] #empty list
    array_length = len(nums)    #just for easier referenceing
  
    for i in range(array_length - 2):
        if i > 0 and nums[i] == nums[i - 1]:    #skip duplicate values to avoid duplicate triplates
            continue
        left, right = i + 1, array_length - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:  #skip duplicates
                    left += 1
                while left < right and nums[right] == nums[right-1]: #skip duplicates
                    right -= 1
                left += 1 #move left pointer right
                right -= 1 #move right pointer left
            elif total < 0: #move left pointer right
                left += 1
            else:   #move right pointer left
                right -= 1
    return result 

testcase1 = [0,1,1]
print(threeSum(testcase1))

testcase2 = [-5, 0, 5, 10, -10, 0]
print(threeSum(testcase2))
#i get duplicate results for this testcase :(