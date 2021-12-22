#Description
"""
Write a function to determine the number of bits you would need to flip to convert integer A
to integer B

Example

Input: 29 (or 11101), 15 (or: 01111)
Output: 2

the easiest solution I can think of is brute force. like, we could go bit by bit 
and check if they are the same. if not, counter++

another approach would be to use an XOR to check the differences in the numbers, and count the number of 1s there
lest do both and check whic hwould be better
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