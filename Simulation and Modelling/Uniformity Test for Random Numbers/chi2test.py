'''Python program to implement a Pseudo Random Number Generator (PRNG) using Linear 
   Congruential Method and to test its uniformity by using Chi Square Test at 0.05
   Level of Significance
   Date: 26/01/2022
   Author: Anurag Ghosh
   -----------------------------
   The program accepts 4 integers as Xo,a,c and m as input
   and generates 100  Pseudo Random Numbers using Linear 
   Congruential Method and and test for the uniformity by using
   Chi Square Test.
'''
#Function generating the random numbers
def linearCongruentialMethod(Xo, m, a, c,randomIntg,noOfRandomNums,randomNums):
    randomIntg[0] = Xo
    for i in range(1, noOfRandomNums):
        randomIntg[i] = ((randomIntg[i - 1] * a) + c) % m

    for i in randomIntg:
        num = round((i/m),2)
        randomNums.append(num)
    
    print("For,\n")
    print("m =",m,"a =",a,"Xo =",Xo,"c =",c)
    
    print("The Random Numbers are as followed : ")
    for i in range (0,100,10):
        print(randomNums[0+i],"\t",randomNums[1+i],"\t",randomNums[2+i],"\t",randomNums[3+i],"\t",
              randomNums[4+i],"\t",randomNums[5+i],"\t",randomNums[6+i],"\t",randomNums[7+i],"\t",
              randomNums[8+i],"\t",randomNums[9+i])
    return randomNums

#Function to count the numbers in a Range
def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr

#Function for performing the Chi Square test for uniformity
def ChiTest(randomList):
    N = len(randomList)
    n = 10
    Ei = N/n
    final = []

    #defining the classes
    Oi = [0]*n

    Oi[0] = count_range_in_list(randomList, 0.00, 0.10)
    Oi[1] = count_range_in_list(randomList, 0.11, 0.20)
    Oi[2] = count_range_in_list(randomList, 0.21, 0.30)
    Oi[3] = count_range_in_list(randomList, 0.31, 0.40)
    Oi[4] = count_range_in_list(randomList, 0.41, 0.50)
    Oi[5] = count_range_in_list(randomList, 0.51, 0.60)
    Oi[6] = count_range_in_list(randomList, 0.61, 0.70)
    Oi[7] = count_range_in_list(randomList, 0.71, 0.80)
    Oi[8] = count_range_in_list(randomList, 0.81, 0.90)
    Oi[9] = count_range_in_list(randomList, 0.91, 1.00)

    for each in Oi:
        final.append(((each-Ei)**2)/Ei)
    
    Chi_o = sum(final)

    #Displaying the Hypothesis and the Chi-Square Table
    print("\nFor the given random numbers, the null and the not null hypothesis are as followed :-")
    print("H\u2080 : R\u1D62 \uFF5E U[0,1]")
    print("H\u2081 : R\u1D62 \u2241 U[0,1]\n")
    
    formatted_row = '{:<8} {:>6} {:>8} {:>8} {:>8}'
    print(formatted_row.format("Intervals","O\u1D62","E\u1D62","(O\u1D62-E\u1D62)",
                               "(O\u1D62-E\u1D62)\u00B2/E\u1D62"))
    for i in range(10):
        print(formatted_row.format(i,Oi[i],Ei,Oi[i]-Ei,final[i]))
    print(formatted_row.format("Total",100,100,"-",round(Chi_o,2)))
    print("\n")
    
    Chi_alpha = 16.9 
    print("\u03C7\u2080\u00B2 : ",round(Chi_o,2),"and \u03C7\u2090\u00B2 : ",Chi_alpha,"\n")

    if(Chi_alpha>Chi_o):
        print("Since,",round(Chi_o,2),"<",Chi_alpha,"i.e., \u03C7\u2080\u00B2 < \u03C7\u2090\u00B2")
        print("H\u2080 is not rejected")
        print("Hence the given random numbers are uniformly distributed between 0 and 1\n")
    else:
        print("Since,",round(Chi_o,2),"\u2265",Chi_alpha,
              "i.e., \u03C7\u2080\u00B2 \u2265 \u03C7\u2090\u00B2")
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
ChiTest(randomList)

#43 128 5 6