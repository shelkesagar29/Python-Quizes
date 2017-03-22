from math import sqrt
def checkprime(num1): #function checking prime
    for i in range(2,int(sqrt(num1))+1): #go from two to square root of that number
        if num1%i==0:
            print("not a prime")
            break
    else:
        print("Prime numeber")

num2=int(input("Enter number:\n"))
checkprime(num2)