import random
def main():
	print("Rolling 4 D6s, summing them without smallest")
	d6roll()
	print("Rolling pair of D10s, sums them")
	d10roll()
	print("Rolling pair of D4s, sums them")
	d4roll()

def diceroll(upper):
    sysrand = random.SystemRandom()
    throw = sysrand.randint(1,upper)
    return throw
def d6roll():


    numbers = []
    for i in range(4):
        throw = diceroll(6)
        numbers.append(throw)
    smallest = numbers[0];
    for x in range(3):
        if(smallest > numbers[x+1]):
            smallest = numbers[x+1]


    print("----------------")
    print(numbers)
    print("Sum without smallest value")
    sum = 0
    for y in numbers:
        sum = sum + y
    sum = sum - smallest
    print(sum)

def d10roll():
    sysrand = random.SystemRandom()
    rand1 = sysrand.randint(1,10)
    rand2 = sysrand.randint(1,10)
    print(rand1, rand2)
    print("Sum")
    print(rand1+rand2)

def d4roll():
    sysrand = random.SystemRandom()
    rand1 = sysrand.randint(1,4)
    rand2 = sysrand.randint(1,4)
    print(rand1, rand2)
    print("Sum")
    print(rand1+rand2)

def statistics():
    rounds = 1000000
    throws = [0,0,0,0,0,0]
    for x in range(rounds):
        roll = diceroll(6)
        throws[roll-1] = throws[roll-1] + 1

    print("Statistics for the d6 is as follows:")
    print("1s: " + str(throws[0]/rounds) + ", " + str(throws[0]) + " occurences")
    print("2s: " + str(throws[1]/rounds) + ", " + str(throws[1]) + " occurences")
    print("3s: " + str(throws[2]/rounds) + ", " + str(throws[2]) + " occurences")
    print("4s: " + str(throws[3]/rounds) + ", " + str(throws[3]) + " occurences")
    print("5s: " + str(throws[4]/rounds) + ", " + str(throws[4]) + " occurences")
    print("6s: " + str(throws[5]/rounds) + ", " + str(throws[5]) + " occurences")




if __name__ == "__main__":
    main()
