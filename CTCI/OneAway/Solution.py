"""
One away: there are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.
"""

def oneAwayReplace(sa:str, sb:str) -> bool:
    limit = False
    for i in range(len(sa)):
        if sa[i] != sb[i]:
            if limit:
                return False
            limit = True
    return True

def oneAwayInsert(sa,sb)->bool:
    i = 0
    j = 0
    while i < len(sa) and j < len(sb):
        if sa[i] != sb[j]:
            if i!=j:
                return False
            j+=1
        else:
            i+=1
            j+=1
    return True

def oneAway(sa:str, sb:str) -> bool:
    sa = sa.replace(" ","")
    sb = sb.replace(" ","")
    if abs(len(sa) - len(sb)) > 1:
        return False
    if len(sa) - len(sb) == 0:
        return oneAwayReplace(sa,sb)
    if len(sa) + 1 == len(sb):
        return oneAwayInsert(sa,sb)
    if len(sa) - 1 == len(sb):
        return oneAwayInsert(sb,sa)
    return False

if __name__ == "__main__":
    sa,sb = "pale","ple"
    print(oneAway(sa,sb))
    assert(oneAway(sa,sb) == True)
    sa,sb = "pales", "pale"
    print(oneAway(sa,sb))
    assert(oneAway(sa,sb) == True)
    sa,sb = "pale", "bale"
    print(oneAway(sa,sb))
    assert(oneAway(sa,sb) == True)
    sa,sb = "pale", "bake"
    print(oneAway(sa,sb))
    assert(oneAway(sa,sb) == False)