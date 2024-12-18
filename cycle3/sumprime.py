upper_limit=int(input("Enter upper limit:"))
for num in range(1,upper_limit+1):
	digit_sum=sum(int(digit) for digit in str(num))
	if digit_sum>1:
		is_prime=True
		for i in range(2,int(digit_sum**0.5)+1):
			if digit_sum%i==0:
				is_prime=False
				break
		if is_prime:
			print(f"The sum of digit {num} is {digit_sum},which is prime") 

