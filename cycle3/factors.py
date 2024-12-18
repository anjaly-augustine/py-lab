n=int(input("Enter the number:"))
div=1
factor=[]
while div<=n:
	if n%div==0:
		factor.append(div)
	div+=1
print(f"Factors of {n}:{factor}") 
