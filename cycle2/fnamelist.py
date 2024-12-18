names=input("Enter the names:")
count=0
for name in names:
	count+=name.count('a')
print(f"The letter a appears {count} times in the list of names")
