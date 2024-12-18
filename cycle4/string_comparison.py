def compare(s1,s2,n):
	if s1[:n]==s2[:n]:
		return True
	else:
		return False
s1=input("Enter a string 1:")
s2=input("Enter string 2:")
n=int(input("Enter the no of terms upto check:"))
if compare(s1,s2,n):
	print("Same")
else:
	print("Different")
