n=int(input("Enter the no of integers you want to enter:"))
int_list=[]
int_list_new=[]
for i in range(n):
	list1=int(input())
	int_list.append(list1)
for num in int_list:
	j=int(num)
	if j>100:
		j="over"
		int_list_new.append(j)
	else:
		int_list_new.append(j)
print(f"The list of integers:{int_list_new}")
