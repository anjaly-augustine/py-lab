def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def calculator():
	while True:
		print("\nChoose the operation:")
		print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
		choice=input("Enter your choice:")
		if choice=='5':
			break
		elif choice in {'1','2','3','4'}:
			num_a=int(input("Enter the number a:"))
			num_b=int(input("Enter the number b:"))
			if choice=='1':
				print("Result:",add(num_a,num_b))
			elif choice=='2':
				print("Result:",sub(num_a,num_b))
			elif choice=='3':
				print("Result:",mul(num_a,num_b))
			elif choice=='4':
				print("Result:",div(num_a,num_b))
			else:
				print("Invalid choice")
calculator()
