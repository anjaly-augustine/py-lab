n=int(input("Enter the number:"))
f1,f2=0,1
for i in range(n):
	print(f"{f1}",end=" ")
	f1,f2=f2,f1+f2
print()
