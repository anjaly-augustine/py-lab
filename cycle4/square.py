area_square=lambda a:a*a
area_rectangle=lambda l,w:l*w
area_triangle=lambda b,h:0.5*(b*h)
a=int(input("Enter side of square:"))
l=int(input("Enter length of rectangle:"))
w=int(input("Enter width of rectangle:"))
b=int(input("Enter base of triangle:"))
h=int(input("Enter height of triangle:"))
print("Area of square:",area_square(a))
print("Area of rectangle:",area_rectangle(l,w))
print("Area of triangle:",area_triangle(b,h))
