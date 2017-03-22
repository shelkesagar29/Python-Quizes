import sys
#Set is an unordered collection of zero or more immutable python data
#objects. This is immutable means can not be changed after declaration
#unlike list
#Set does not allow duplicates

myset={3,6,"cat",4.5,False}
print(myset)
print(len(myset))#print length of set
print(6 in myset)# check for 6 in set and return either true or false

yourset={99,3,100}
print (yourset)
print(myset.union(yourset))#Return a new set with all emements from both sets
print(myset.intersection(yourset))# return intersection
print(myset|yourset)
print(myset.difference(yourset))#all elemnets from first set that are not in
#second set
print(myset.issubset(yourset))# gives true or false
myset.add(9)# we cant change elements but can add
print(myset)
myset.remove(4.5)
print(myset)