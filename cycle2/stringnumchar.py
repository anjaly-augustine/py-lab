char_c=input("Enter a string:")
char_count={}
for char in char_c:
	if char in char_count:
		char_count[char]+=1
	else:
		char_count[char]=1
print(f"Character frequency of {char_c}is{char_count}")

