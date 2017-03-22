name=input("Give me your name: ")
print("Your name is "+name)
try:age=int(input("Enter your age: "))
except ValueError:
    print("Oops! It seems you have not entered number")
print("You are ",name,"and you are",age,"years old" )
yea=100-age
print("After",yea,"years, you will become 100 years old")