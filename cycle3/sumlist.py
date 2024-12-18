n=int(input("Enter the no of elements:"))
list=[]
sum=0
for i in range(n):
	list1=int(input())
	list.append(list1)
for i in list:
	sum+=i
print(f"Sum:{sum}")
