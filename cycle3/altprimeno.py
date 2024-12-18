n=int(input("Enter a positive integer:"))
prime=[]
for num in range(2,n+1):
	is_prime=True
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			is_prime=False
			break
	if is_prime:
		prime.append(num)
for i in range(0,len(prime),2):
	print(prime[i],end=" ")
print()
