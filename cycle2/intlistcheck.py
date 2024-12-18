n=int(input("Enter no of integers to input:"))
list1=[]
for i in range(n):
	num=int(input("Enter integers:"))
	list1.append(num)
n=int(input("Enter no of integers to input:"))
list2=[]
for i in range(n):
	num=int(input("Enter integers:"))
	list2.append(num)
if len(list1)==len(list2):
	print("Lists are of same length")
else:
	print("Lists are of different length")
if sum(list1)==sum(list2):
	print("The list sum to the same value")
else:
	print("The lists don't sum to same value")
common_value=set(list1).intersection(list2)
if common_value:
	print(f"Common values:{common_value}")
else:
	print(f"No common values")
