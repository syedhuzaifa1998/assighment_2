print("Enter any number ")
num1=int(input())
if(num1==0):
    print("Neither EVEN nor ODD")
if(num1%2==0 and num1!=0):
    print("Number Is EVEN")
if(num1%2!=0 and num1!=0):
    print("Number Is ODD")