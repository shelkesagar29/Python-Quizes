list1=[1,2,3,4]

def listman(list1):#passing list to function
    list2=[]
    list2.append(list1.pop(0))
    list2.append(list1.pop())
    return list2

list2=listman(list1)
print(list2)

#if you passed list like below
# listman(*list1)
#Function considers each list item as a seperate parameter
#have look into other file