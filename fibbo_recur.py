def fibo(n):
    if n<=1: #every recursive function should ahve a base condition, otherwise it will go in infinite loop
        return n
    else:
        return(fibo(n-1)+fibo(n-2)) #rescursive call to function

nterms=int(input("Enter number of terms you want in Fibonacci:\n"))
if nterms<=0:
    print("Make sure input is positive")
else:
    for i in range(nterms):
        print(fibo(i))