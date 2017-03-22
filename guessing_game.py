import sys
import random

guess=1 #count number of time we are guessing for one bingo
while True:
    
    inum=int(input("Enter any number between 1 and 9(including)\n"))
    rnum=random.randint(1,9)
    print(rnum)
    if (abs(rnum-inum)==0):
        print("Bingo! You got it...\n")
    else:
        print("you are",abs(rnum-inum),"units away from actual number\n")
    print("This was trial no:",guess)
    wish=input("Do you want to continue? (y/n)\n")
    if wish=='n':
        break
    else:
        guess+=1
        pass