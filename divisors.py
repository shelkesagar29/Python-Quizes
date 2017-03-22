import sys
num=int(input("Enter number for which you want to find divisors:\n"))
list2=[]
for i in range(1,num+1):
    if (num%i==0):
        list2.append(i)
    else:
        pass
print (list2)

# Writting in two lines
#import sys
#num=int(input("Enter number for which you want to find divisors:\n"))
#list2=[x for x in range(1,num+1) if (num%x==0)]
#print (list2)    