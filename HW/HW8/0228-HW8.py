# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


def longestPalindrome(s):
    hm = {} # hashmap: string = key, count = value
    len = 0 # length of longestpalindrome
    is_odd = False  # if there is an odd count

    #initialize hashmap
    for char in s:
        if char in hm:
            hm[char] += 1
        else:
            hm[char] = 1

    # calculations
    for count in hm.values():
        len += count // 2 * 2
        if count % 2 != 0:
            is_odd = True
            
    if is_odd:
        len += 1
        
    return len  # return length


testcase1 = "abcccdd"
print(longestPalindrome(testcase1))

testcase2 = "speediskey"
print(longestPalindrome(testcase2))