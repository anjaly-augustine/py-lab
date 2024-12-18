n=int(input("Enter the size:"))
for i in range(1,n+1):
	if i!=n:
		print("*"*i,end=' ')
		print()
	else:
		for i in range(n,0,-1):
			print("*"*i,end=' ')
			print()
