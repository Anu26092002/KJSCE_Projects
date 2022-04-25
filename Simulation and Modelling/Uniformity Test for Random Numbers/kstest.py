'''Python program to implement a Pseudo Random Number Generator (PRNG) using Linear 
   Congruential Method and to test its uniformity by using Kolmogorov-Smirnov Test
   at 0.05 Level of Significance.
   Date: 24/01/2022
   Author: Anurag Ghosh
   -----------------------------
   The program accepts 4 integers as Xo,a,c and m as input
   and generates 100  Pseudo Random Numbers using Linear 
   Congruential Method and test for the uniformity by using
   Kolmogorov-Smirnov Test.
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
    print("For,\n")
    print("m =",m,"a =",a,"Xo =",Xo,"c =",c)
    
    print("The Random Numbers are as followed : ")
    for i in range (0,100,10):
        print(randomNums[0+i],"\t",randomNums[1+i],"\t",randomNums[2+i],"\t",randomNums[3+i],"\t",randomNums[4+i],"\t",randomNums[5+i],"\t",randomNums[6+i],"\t",randomNums[7+i],"\t",randomNums[8+i],"\t",randomNums[9+i])
    return randomNums

def KSTest(randomList):
    N = len(randomList)
    Dalpha = 1.36/(math.sqrt(N))
    randomList.sort()
    
    ibyN = []
    for i in range(N):
        ibyN.append((i+1)/N)
    
    Dtable1 = []
    for i in range(N):
        Dtable1.append(ibyN[i]-randomList[i])

    Dtable2 = []
    for i in range(N):
        Dtable2.append(randomList[i]-(i/N))

    Dplus = max(Dtable1)
    Dminus = max(Dtable2)
    D =  max(Dplus,Dminus)

    #Displaying the Hypothesis and the Kolmogorov-Smirnov Table
    print("\nFor the given random numbers, the null and the not null hypothesis are as followed :-")
    print("H\u2080 : R\u1D62 \uFF5E U[0,1]")
    print("H\u2081 : R\u1D62 \u2241 U[0,1]\n")

    formatted_row = '{:<8} {:>6} {:>8} {:>8} {:>8}'
    print(formatted_row.format("i","R\u1D62","i/N","i/N - R\u1D62","R\u1D62 - (i-1)/N"))
    for i in range(N):
        print(formatted_row.format(i+1,randomList[i],round(ibyN[i],4),round(Dtable1[i],4),round(Dtable2[i],4)))
    print("\n")
    
    print("D+ =",Dplus,"D- =",Dminus)
    print("D =",round(D,2),"and D\u2090 =",Dalpha,"\n")

    if(Dalpha>D):
        print("Since,",round(D,3),"<",Dalpha,"i.e., D < D\u2090")
        print("H\u2080 is not rejected")
        print("Hence the given random numbers are uniformly distributed between 0 and 1\n")
    else:
        print("Since,",round(D,3),"\u2265",Dalpha,"i.e., D \u2265 D\u2090")
        print("H\u2080 is rejected")
        print("Hence the given random numbers are not uniformly distributed between 0 and 1\n")



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
KSTest(randomList)