import math
a=int(input("Enter coefficient a:"))
b=int(input("Enter coefficient b:"))
c=int(input("Enter coefficient c:"))
d=(b**2)-4*a*c
if d>0:
	root1=(-b+math.sqrt(d))/(2*a)
	root2=(-b-math.sqrt(d))/(2*a)
	print("Two real roots:",root1,root2)
elif d==0:
	root=-b/(2*a)
	print("One real root:",root)
else:
	real=-b/(2*a)
	img=math.sqrt(-d)/(2*a)
	print(f"Two complex roots:{real}+{img}i and {real}-{img}i")
