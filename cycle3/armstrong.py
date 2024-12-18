n=int(input("Enter the number:"))
num=n
sum=0
while n>0:
	r=n%10
	sum+=r**3
	n//=10
if num==sum:
	print(f"{num} is armstrong")
else:
	print(f"{num} is not armstrong")

