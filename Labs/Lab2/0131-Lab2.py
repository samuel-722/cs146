def anagram(t, s):
    t_hm = {} #initialize empty hashmap for t
    s_hm = {} #initialize empty hashmap for s
    for character in t:
        if character in t_hm:
            t_hm[character] += 1
        else:
            t_hm[character] = 1
    for character in s:
        if character in s_hm:
            s_hm[character] += 1
        else:
            s_hm[character] = 1

    return(t_hm == s_hm)

sentence = "secure"
tsentence = "rescue"
if anagram(tsentence, sentence):
    print("the two strings are anagrams")
else:
    print("not anagrams")
