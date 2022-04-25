'''Python program to implement a Pseudo Random Number Generator (PRNG) using Linear 
   Congruential Method and to test its independence by using Runs up and Down Test
   at 0.05 Level of Significance.
   Date: 31/01/2022
   Author: Anurag Ghosh
   -----------------------------
   The program accepts 4 integers as Xo,a,c and m as input
   and generates 100  Pseudo Random Numbers using Linear 
   Congruential Method and test for the independence by 
   using Runs up and Down Test.
'''

#importing the math module for sqrt function
import math

#Function generating the random numbers
def linearCongruentialMethod(Xo, m, a, c,randomIntg,noOfRandomNums,randomNums):
    randomIntg[0] = Xo
    for i in range(1, noOfRandomNums):
        randomIntg[i] = ((randomIntg[i - 1] * a) + c) % m

    for i in randomIntg:
        num = round((i/m),2)
        randomNums.append(num)

    #Displaying the Random Numbers
    print("\nFor,")
    print("m =",m,"a =",a,"Xo =",Xo,"c =",c)
    
    print("The Random Numbers are as followed : ")
    for i in range (0,100,10):
        print(randomNums[0+i],"\t",randomNums[1+i],"\t",randomNums[2+i],"\t",randomNums[3+i],
              "\t",randomNums[4+i],"\t",randomNums[5+i],"\t",randomNums[6+i],"\t",
              randomNums[7+i],"\t",randomNums[8+i],"\t",randomNums[9+i])
    return randomNums

def runLength(runs):
    counter = 1
    for i in range(len(runs)-1):
        if runs[i] != runs[i+1]:
            counter += 1
    return counter

def RunsUpAndDownTest(randomList, alpha):
    N = len(randomList)
    runs=[]
    for i in range(len(randomList)-1):
        if randomList[i] < randomList[i+1]:
            runs.append('+')
        else:
            runs.append('-')

    print("The sequence of Runs up and down is as followed:\n")
    for ch in runs:
        print(ch+" ",end="")

    a = runLength(runs)
    mew_a = (2*N-1)/3
    sigma_a = math.sqrt((16*N-29)/90)
    Zo = ((a-mew_a)/sigma_a)
    
    print("\n\nHere,")
    print("N =",N,"a =",a,"\u03BC\u2090 =",round(mew_a,3),"\u03C3\u2090 =",round(sigma_a,3),
          "Z\u2080 =",round(Zo,3),"\u03B1 =",alpha)
    if alpha == 0.05:
        Zalphaby2p = 1.96
        Zalphaby2m = -1.96

    #Displaying the Hypothesis
    print("\nFor the given random numbers, the null and the not",
          "null hypothesis are as followed :-")
    print("H\u2080 : R\u1D62 \uFF5E independent")
    print("H\u2081 : R\u1D62 \u2241 independent\n")

    if(Zo >= Zalphaby2m and Zo <= Zalphaby2p):
        print("Since,",Zalphaby2m,"\u2264",round(Zo,3),"\u2264",Zalphaby2p,
              "i.e., -Z\u2090\u2097\u2082 \u2264 Z\u2080 \u2264 Z\u2090\u2097\u2082")
        print("H\u2080 is not rejected")
        print("Hence the given random numbers are independently distributed.\n")
    else:
        print("Since,",round(Zo,3),"\u2209 [",Zalphaby2m,",",Zalphaby2p,
              "] i.e., Z\u2080 \u2209 43[-Z\u2090\u2097\u2082 ,Z\u2090\u2097\u2082]")
        print("H\u2080 is rejected")
        print("Hence the given random numbers are not independently distributed.\n")

randomNums = []
noOfRandomNums = 100
randomIntg = [0] * (noOfRandomNums)

#Try except block to handle the errors
try:
    # Seed value
    Xo = int(input("\nEnter the Seed value(Xo) : "))
        
    # Modulus parameter
    m = int(input("\nEnter the Modulus parameter(m) : "))
            
    # Multiplier term
    a = int(input("\nEnter the Multiplier term(a) : "))
        
    # Increment term
    c = int(input("\nEnter the Increment term(c) : "))

    #Checking of the conditions of Linear congurential Method
    if m <= 0 or a <= 0 or c < 0 or Xo < 0 or a >= m or c >= m or Xo >= m:
        raise ValueError

except ValueError:
    print("The values should be integers such that 0 < m, 0 < a < m, 0 <= c < m and 0 <= Xo < m")

randomList = linearCongruentialMethod(Xo, m, a, c,randomIntg,noOfRandomNums,randomNums)
alpha = 0.05
RunsUpAndDownTest(randomList,alpha)

# m = 2147483647 a = 16807 Xo = 123457 c = 0