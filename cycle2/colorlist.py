n=int(input("Enter the no of colors you want to enter:"))
color_list1=[]
color_list2=[]
color_list=[]
print("Enter the color list1:")
for i in range(n):
	list1=input()
	color_list1.append(list1)
print("Enter the color list2:")
for i in range(n):
	list2=input()
	color_list2.append(list2)
for color in color_list1:
	if color not in color_list2:
		color_list.append(color)
print(f"Color in colorlist1 that are not contained in color list2 are {color_list}")
