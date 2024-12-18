def factorial(num):
	fact=1
	for i in range(1,num+1):
		fact*=i
	return fact
n=int(input("Enter the number of terms:"))
sum=0
for i in range(1,n+1):
	sum+=(i**i)/factorial(i)
print(f"Sum of series: {sum}")
