string=input("Enter word to check for palindrome\n")
rev=string[::-1]
if string==rev:
    print("Palindrome")
else:
    print("not palindrome")