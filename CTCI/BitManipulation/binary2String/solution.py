#Description
"""
Given a real number between 0 and 1 that is passed in as a double, print the binary representation. 
If the number cannot be represented accurately in binary with at most 32 characters, print "Error".
Solution: 

I believe that the best way to solve it would be to check recursively if the binary number is larger than the current number,
and to add 1 or 0 to an array, and then print that number. something like this

lets represent 0.75.

Then to represent it it would be something like: 
first position on the right of the decimal point is NUMBER*1/2 so 0.5
is 0.5 < 0.75? yes. 
therefore, 1 must be added to an array
and the new number is 0.75-0.5 = 0.25
the next number is NUMBER*1/4 so 0.25
so is 0.25<= 0.25? yes. therfore, we add a 1, and we finish
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
    n = 0.72
    print(binary2String(n))