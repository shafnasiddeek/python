def perfectsquare(l,r):
    for i in range(l,r+1):
     if (i**(.5)==int(i**(.5))):
            print(i,end=" ")
l=int(input("enter the first number"))
r=int(input("enter the last number"))
perfectsquare(l,r)
