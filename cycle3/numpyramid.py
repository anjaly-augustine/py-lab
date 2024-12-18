n=int(input("Enter the size:"))
num=1
for i in range(1,n+1):
	for j in range(1,num+1):
		x=i*j
		print(x,end=' ')
	num+=1
	print()
