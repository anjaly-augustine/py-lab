def check_prime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True
def is_prime(pos):
	n=2
	count=0
	while True:
		if check_prime(n):
			count+=1
			if count==pos:
				return n
		n+=1
pos=int(input("Enter the position:"))
prime=is_prime(pos)
print(f"The prime number at position {pos}:{prime}")
