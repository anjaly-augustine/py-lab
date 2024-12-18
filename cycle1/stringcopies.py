org_string=input("Enter a string:")
n=int(input("Enter a non negative integer:"))
if n>0:
	result=org_string*n
	print(f"The resulting string is:{result}")
else:
	print("Please enter a non-negative integer")
