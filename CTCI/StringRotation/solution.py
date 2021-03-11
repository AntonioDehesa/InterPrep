"""
assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1, using only one call to isSubstring
example: "waterbottle" is a rotation of "erbottlewat"
"""


def isSubstring(s1:str, s2:str) -> bool:
    if len(s1) != len(s2):
        return False
    i = s2.index(s1[0])
    for char in s1:
        if i >= len(s2):
            i = 0
        if char != s2[i]:
            return False
        i += 1
    return True
if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    result = isSubstring(s1,s2)
    print(result)