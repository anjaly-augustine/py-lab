n=int(input("Enter the limit:"))
sum=0
for i in range(n):
	if i%6==0 and i%4!=0:
		sum+=i
print(f"Sum:{sum}")
