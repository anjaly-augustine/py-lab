n=int(input("Enter the no of words:"))
wordlist=[]
for i in range(n):
	word=input("Enter words:")
	wordlist.append(word)
maxlength=0
for i in wordlist:
	if len(i)>maxlength:
		maxlength=len(i)
		word=i
print("Longest word:",word)
print("Length of the longest word:",maxlength)
