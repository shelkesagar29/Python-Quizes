import random

charkeys="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numkeys="01234567890"
speckeys="@$%^&*()"

def givepass(a,b,c):
    retchar=random.sample(charkeys,a)
    retnum=random.sample(numkeys,b)
    retspec=random.sample(speckeys,c)
    retchar.extend(retnum+retspec)#append all lists together
    return(''.join(retchar))
#ask your for how many number,char and special char they want in passenger

while True:
    numchar=int(input("Number of characters you expect in your passowrd\n"))
    numnum=int(input("Number of numers you expect in your passowrd\n"))
    numspechar=int(input("Number of special characters you expect in your passowrd\n"))
    print("Your password is:\n",givepass(numchar,numnum,numspechar))
    cont=input("Want another password?(y/n)\n")
    if cont=='y':
        inp2=input("Should we use last specifications again? (y/n)\n")
        if inp2=='y':
            print("Your password is:\n",givepass(numchar,numnum,numspechar))
            cont=input("Want another password?(y/n)\n")
            if cont=='y':
                pass
            else: break                
        else: pass
    else:
        break

print("Thank you for using our service. Have a nice day!")