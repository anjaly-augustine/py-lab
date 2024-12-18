n=int(input("Enter the no of integers you want to enter:"))
odd_list=[]
list1=[]
for i in range(n):
	num_list=int(input())
	list1.append(num_list)
for num in list1:
	j=int(num)
	if j%2!=0:
		odd_list.append(j)
print(f"The list after removing even numbers:{odd_list}")
