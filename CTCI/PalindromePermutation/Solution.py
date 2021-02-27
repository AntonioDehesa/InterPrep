"""
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearragement of letters. 
The palindrome does not need to be limited to just dictionary words.
Example
Input: Tact Coa
Output: True (Permutations: taco cat, atco cta, etc)
"""


def checkPermutation(s:str) -> bool:
    s = s.lower()
    s = s.replace(" ","")
    #s.lower()
    limitForMiddleChar = False
    myDict = {}
    for char in s:
        myDict[char] = myDict.get(char, 0) + 1
    print(myDict)
    for key in myDict:
        if myDict[key]%2 != 0:
            if limitForMiddleChar:
                return False
            limitForMiddleChar = True
    print(s)
    return True


if __name__ == "__main__":
    s = "TACT coa"
    print(checkPermutation(s))
