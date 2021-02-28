"""
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller
than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).
"""

def compression(s:str)->str:
    temp = s[0]
    counter = 0
    result = ""
    for char in s:
        if char != temp:
            result = result + "{}{}".format(temp,counter)
            temp = char
            counter = 1
        else:
            counter += 1
    result = result + "{}{}".format(temp,counter)
    print(result)
    return result if len(result) < len(s) else s

if __name__ == "__main__":
    s = "aabcccccaaa"
    result = compression(s)
    assert(result == "a2b1c5a3")