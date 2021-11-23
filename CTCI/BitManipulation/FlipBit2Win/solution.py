#Description
"""
You have an integer and you can flip exactly one bit from 0 to a 1. 
Write code to find the length of the longest sequence of 1s you could create.

Example: 
Input: 1775 (or 11011101111)
Output: 8

Solution:
We can go through the input, and check what is the longest sequence of 1s, and check those sequences of one
that are divided only by one 0. In the example we can see that the longest sequence is of four consecutive 1s. 
the sequences that are divided by only one 0 are the sequence of 4 1s and 3 1s, the sequence of 3 1s and 2 1s.
that way, if we add the sequences plus 1, we get
4 + 3 + 1 = 8
3 + 2 + 1 = 6

the longest is 8. is 8 longer than the longest sequence (4) plus 1? 
4 + 1 = 5 
so yes, in this case

ok, so lets start
"""

def flipBit2Win(input: str) -> int:#Input = 11011101111 for tests
    max = 0
    current = 0
    sequence = 0
    for i in range(len(input)):
        try:
            if( input[i] == "1"):
                current+=1
            elif (input[i+1] == "1"):
                max = current if current > max else max
                sequence = current + sequence
                max = sequence if sequence > max else max
                sequence = current
                current = 0
            else:
                sequence = 0
        except:
            break
    seq = sequence + current
    res = max if max > seq else seq
    return res+1

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

def binary2String(number: int):
    result = []
    multiplier = 1/2
    while number > 0:
        if multiplier <= number:
            result.append("1")
            number-=multiplier
        else:
            result.append("0")
        multiplier*=1/2
    res = ""
    for n in result:
        res+=n
    return "0." + res


if __name__ == "__main__":
    input = "11011101111"
    result = flipBit2Win(input=input)
    print(result)
    assert(result == 8)
    input2 = "1010110100110101110111010001111111010010"
    result = flipBit2Win(input=input2)
    print(result)
    assert(result == 9)