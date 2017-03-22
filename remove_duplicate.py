a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]

#general structure of list comprehention is
#[expression for_LOOPS condition_loops]

list1=[x for x in a if x in b] #gives list with duplicates
list2=[]
#logic to remove duplicates from given list and make new list
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(list2)