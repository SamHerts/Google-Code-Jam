"""
Someone just won the Code Jam lottery, and we owe them N jamcoins! However, when we tried to print out an oversized check, 
we encountered a problem. The value of N, which is an integer, includes at least one digit that is a 4... 
and the 4 key on the keyboard of our oversized check printer is broken.

Fortunately, we have a workaround: we will send our winner two checks for positive integer amounts A and B, 
such that neither A nor B contains any digit that is a 4, and A + B = N. Please help us find any pair of values A and B that satisfy these conditions.

Sample Input:
3 -- Number of cases to be tested
4 -- case 1
940 -- case 2
4444 -- case 3

Sample Output:
Case #1: 2 2
Case #2: 852 88
Case #3: 667 3777
"""
tests = int(input())


def solver():
    n = str(input())
    pos = []
    subber = 0
    for i in range(len(n)): #Get positions of number 4
        if n[i] == "4":
            pos.append(1)
        else:
            pos.append(0)
    t = 0
    for i in pos[::-1]:    # Reverse over positions and add powers of 10 where necessary    
        subber += (10**t)*i
        t += 1
    
    if len(pos) == 0:
        return [0,n]
    return [subber, int(n) - subber] # Return the power of 10 and subtracted value


for outp in range(tests):
    value = solver()
    print("Case #%d: %s %s" % (outp+1, value[0], value[1]) )
