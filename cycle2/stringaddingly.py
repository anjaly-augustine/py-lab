string1=input("Enter the string:")
if string1[-3:]!="ing" and string1[-2:]!="ly":
	out_string=string1+"ing"
elif string1[-2:]=="ly":
	out_string=string1
else:
	out_string=string1+"ly"
print(out_string)
