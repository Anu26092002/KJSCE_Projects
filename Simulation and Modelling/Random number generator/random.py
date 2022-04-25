'''Python program to implement a Pseudo Random Number Generator (PRNG) using Linear 
   Congruential Method
   Date: 22/01/2022
   Author: Anurag Ghosh
   -----------------------------
   The program accepts 4 integers as Xo,a,c and m as input
   and generates 100  Pseudo Random Numbers using Linear 
   Congruential Method and it also calculates the periodicity
   and density of the Random Numbers.
'''

#importing the math module for the log, ceil and floor function
import math

#Function to calculate log to base 2
def Log2(x):
    return (math.log10(x) / math.log10(2))

#Function to check wether the number is a power of two or not
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

#Function to check wether the number is a prime or not
def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

#Function to check wether two number are relatively prime or not
def isRelativelyPrime(c,m):
    mn = min(c, m) 
    for i in range(1, mn+1):
        if c%i==0 and m%i==0:
            hcf = i 
    
    if hcf == 1:
        return True
    return False

#Function generating the random numbers
def linearCongruentialMethod(Xo, m, a, c,randomIntg,noOfRandomNums):
    randomIntg[0] = Xo
    for i in range(1, noOfRandomNums):
        randomIntg[i] = ((randomIntg[i - 1] * a) + c) % m

#Function to calculate the average difference between the random numbers
def avgDiff(randomNums,noOfRandomNums):
    diff=[]
    for i in range(0, noOfRandomNums-1):
        diff.append(abs(randomNums[i]-randomNums[i+1]))

    return sum(diff) / len(diff)

# Driver Code
if __name__ == '__main__':
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
        
        if isPowerOfTwo(m)!=True and isprime(m)!=True :
            raise TypeError
    except ValueError:
        print("The values should be integers such that 0 < m, 0 < a < m, 0 <= c < m and 0 <= Xo < m") 
    except TypeError:
        print("The Period cannot be calculated if m is not a power of two and composite") 
    except Exception:
        print("OOPs! Something went wrong please try again :(")   
    else:
        p = 0
        randomNums = []
        noOfRandomNums = 100
        b = math.log(m,2)

        randomIntg = [0] * (noOfRandomNums)
    
        linearCongruentialMethod(Xo, m, a, c,randomIntg,noOfRandomNums)
    
        for i in randomIntg:
            num = round((i/m),2)
            randomNums.append(num)
        
        #Calculating the periodicity as per different conditions
        if isPowerOfTwo(m) and m == 2**b and c!=0 and isRelativelyPrime(c,m) and a%4==1:
            p = m
        elif isPowerOfTwo(m) and m == 2**b and c==0 and Xo%2==1 and (a%8==3 or a%8==5):
            p = 2**(b-2)
        elif isprime(m) and c==0 and ((a**(m-1))-1)%m==0:
            p = m - 1
        
        #Displaying the values and the generated random integers and numbers
        print("\nm =",m,"a =",a,"Xo =",Xo,"c =",c)
        print("\nThe Random Integers are as followed : ")
        for i in randomIntg:
            print(i, end = " ")

        print("\n\nThe Random Integers are as followed : ")
        for i in randomNums:
            print(i, end = " ")

        print("\nperiod :",int(p))
        print("\nDensity :",round((avgDiff(randomNums,noOfRandomNums)/p),4))
        print("\n")
