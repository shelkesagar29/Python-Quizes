a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
list3=[]
for i in range(len(a)):
    for j in range(len(b)):
        if (a[i]==b[j]and a[i] not in list3):#compare with b and check if not in a
            list3.append(a[i])
        else:
            pass
print (list3)