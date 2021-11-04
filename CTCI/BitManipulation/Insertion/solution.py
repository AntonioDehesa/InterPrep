#Description
"""
You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
Write a method to insert M into N such that M starts at bit j and ends at bit i. 
You can assume that the bits j through i have enough space to fit all of M. 
That is, if M = 10011, you can assume that there are at least 5 bits between j and i. 
You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2. 
Example: 
Input N = 10000000000, M = 10011, i = 2, j = 6
Output N = 10001001100


So first we have to clean the bits between i and j. Then we can start adding the new bits to the number.
We can create a number that is 1 followed by (j-i+1) trailing 0s. Then we shift it left i times, with trailing 1s. 
Then we do a AND. that way, they are clean.

We could do this by first coping the M number, left shifting it by i, and then negating it. 
"""

def clearBit(numberToInsert: int,numberToClean: int, start: int, end: int):
    allOnes = 0xFF
    mask = (allOnes << (end+1)) & 0xFF | ((1 << start) - 1)
    numberToClean = numberToClean & mask
    return numberToClean | numberToInsert << start

def decitoBin(numb):
    # checking if the given number is greater than 1
    if numb > 1:
        # if it is greater than 1 then use recursive approach by dividing number by 2
        decitoBin(numb // 2)
    # printing the binary representation of the given number
    print(numb % 2, end='')
if __name__ == "__main__":
    M = 10011
    n = 10000000000
    i = 2
    j = 4
    res  = clearBit(M,n,i,j)
    print(res)
    decitoBin(res)