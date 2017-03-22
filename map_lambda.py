import sys
#Python has special way of performing repeated function calls.
# if you want to apply he same function to every element of a list
#the dont loop like normal programmer.
#Instead use map amd lambda functions.
# map(function,list). Lambda function can execute only one command.

list1=[1,2,3,4]

list2=list(map(lambda x:pow(x,2)+7,list1))
print (list2)

#filter is used to filter value from list

list3=list(filter(lambda x:x>3,list1))
print(list3)