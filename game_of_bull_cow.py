import random

def retrand(n):
    rand_start=10**(n-1)
    rand_end=(10**n)-1
    return(random.randint(rand_start,rand_end))

if __name__=="__main__":
    trial=1
    nin=int(input("Enter number of digits you want to play with!\n"))
    recint=(retrand(nin))
    print ("Random number generated is: ",recint)
    while True:
        print("Trial:",trial) 
        usein=input("Enter your number\n")
        compa=str(recint)
        cows=0
        bulls=0
        arra=[]
        for i in range(nin):
            if compa[i]==usein[i]:
                cows+=1
                arra.append(i)
            else:
                bulls+=1

        print("cows=",cows,"bulls=",bulls)
        trial+=1
        uin=input("Do you want to continue?(y/n)\n")
        if uin=='y':
            pass
        else:
            break