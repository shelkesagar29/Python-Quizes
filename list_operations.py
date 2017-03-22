import sys
list1=[1,2,3,4,5,6,7,8,9]
list1.append(10)#adds new item to the end of the list
print(list1)
list1.insert(3,15)#insert new item at given index
print(list1)
print(list1.pop())#Removes and resturns last item in a list
print(list1)
print(list1.pop(2))#Removes and returns element at ith position
print(list1.sort())#print sorted list
print(list1.reverse())#reverse. To get descending order, first sort and then reverse
del list1[0]
print (list1)
