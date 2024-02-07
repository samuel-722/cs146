def palindrome(s):
    userString = s.lower().replace(" ","")
    reverseString = userString[::-1]
    if (reverseString == userString):
        print("this is a palindrome :)")
    else:
        print("this is not a palindrome :(")

userInput = "do GEEse See goD"
palindrome(userInput)