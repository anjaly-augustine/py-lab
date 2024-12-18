import math
start=int(input("Enter starting value:"))
end=int(input("Enter ending value:"))
result=[]
for num in range(start,end+1):	
	if num>=1000 and num<=9999:
		if int(math.sqrt(num))**2==num:
			all_even=True
			for digit in str(num):
				if int(digit)%2!=0:
					all_even=False
					break
			if all_even:
				result.append(num)
print(f"The four digit numbers in the range {start} to {end} are:")
print(result)
