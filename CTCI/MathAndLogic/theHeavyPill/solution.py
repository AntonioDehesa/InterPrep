#Description
"""
You have 20 bottles of pills. 19 bottles have 1.0 gram pills, 
but one has pills of weight 1.1 grams.
Given a scale that provides an exact measurement, how would you find the heavy bottle? 
You can only use the scale once. 

There is no code in this problem. 
I read the solution. wow

I seriously did not think about it. but i guess that i did not understand the question.
it said that it had pills of 1 and 1.1 grams. i thought that each bottle weighted 1 or 1.1 
grams. 
"""
def pairWiseSwap(input: int):
    a = ((input & 0x5555) << 1)
    b = ((input & 0xAAAA) >> 1)
    return a | b

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
    input = 15
    print(pairWiseSwap(input))