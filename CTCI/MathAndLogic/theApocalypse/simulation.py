from random import randrange


def coupleSimulation():
    boys = 0
    girls = 0
    while girls == 0:
        if(randrange(2) == 1):
            girls+=1
        else:
            boys+=1
    return girls,boys

def familySimulation(couples: int):
    girls = 0
    boys = 0
    for couple in range(couples):
        res = coupleSimulation()
        girls+=res[0]
        boys+=res[1]
    return girls,boys

if __name__ == "__main__":
    input = 10000
    res = familySimulation(input)
    print("Girls: {}".format(res[0]))
    print("Boys: {}".format(res[1]))
    print("Proportion: {}".format(res[0]/res[1]))