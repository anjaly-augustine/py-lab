a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
c=int(input("Enter third no:"))
if(a>b and a>c):
	print(a,"is the largest")
elif(b>c and b>a):
	print(b,"is the largest")
else:
	print(c,"is the greatest")
