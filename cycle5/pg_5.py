
from graphics.rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter
from graphics.three_d_graphics.cuboid import *
from graphics.three_d_graphics.sphere import *

length = float(input("Enter Length of Rectangle: "))
width = float(input("Enter Width of Rectangle: "))
print("Rectangle Area :", rectangle_area(length, width))
print("Rectangle Perimeter :", rectangle_perimeter(length, width))
print()

radius = float(input("Enter Radius of Circle: "))
print("Circle Area :", circle_area(radius))
print("Circle Perimeter :", circle_perimeter(radius))
print()

length = float(input("Enter Length of Cuboid: "))
width = float(input("Enter Width of Cuboid: "))
height = float(input("Enter Height of Cuboid: "))
print("Cuboid Area :", cuboid_area(length, width, height))
print("Cuboid Volume :", cuboid_volume(length, width, height))
print()

radius = float(input("Enter Radius of Sphere: "))
print("Sphere Area :", area(radius))
print("Sphere Volume :", volume(radius))






