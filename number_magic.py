import sys
class numbermagic:
    
    def __init__(self,num1,num2): #class constructor 
        self.num1=num1
        self.num2=num2

    def oddoreven(self):#method to check odd or even
        if (self.num1%2)==0:
            print(self.num1,"is even")
        else: print(self.num1,"is odd")
        if (self.num2%2)==0:
            print(self.num2,"is even")
        else: print (self.num2,"is odd")

    def dividefour(self): #method to check whether both numbers are divisible by four
        if((self.num1%4)==0 and (self.num2%4==0)):
            print ("both numbers are divided by four")
        else:
            if(self.num1%4)==0:
                print(self.num1,"is divided by four")
            elif(self.num2%4)==0:
                print(self.num2,"is divisible by four")

inputu=input("Enter two numbers seperated by comma:\n")#reading values
data=inputu.split(',')
inplist=[int(x.strip()) for x in data]
numb1=inplist[0]
numb2=inplist[1]
print (numb1)
print (numb2)
obj1=numbermagic(numb1,numb2)#instantiate class
obj1.oddoreven()
obj1.dividefour()