#Description
"""
You have a basketball hoop and someone says that you can play one of two games. 
Game 1: You get one shot to make the hoop
Game 2: You get three shots and you have to make two of three shots. 

If p is the probability of making a particular shot, 
for which values of p should you pick one game or the other

Game 1: 
The probability is P

Game 2: 
The probability depends on:
If we have to make 2/3 or at least 2/3. 

If exactly 2/3:
G2: P(1 and 2 but no 3) + P(1 and 3 but no 2) + P(3 and 2 but no 1)
G2: (P*P*(1-p))*3
G2: 3(P²-P³)

If at least 2/3:
G2: P(1 and 2 but no 3) + P(1 and 3 but no 2) + P(3 and 2 but no 1) + P³
G2: (P*P*(1-p))*3 + P³
G2: 3(P²-P³) + P³
G2: 3P² - 2P³

so

If 1
G1 > G2?
P = 3P² - 3P³
P + 3 P³ - 3P² = 0
1 + 3P² - 3P = 0

Cannot be solved with real numbers...

If 2
G1 = G2
P = 3P² - 2P³
P + 2P³ - 3P² = 0
1 + 2P² - 3P = 0
two solutions: P = 1/2 or P = 1

So if 0 < P < 1/2 G1
if 1/2 < P < 1 G2
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