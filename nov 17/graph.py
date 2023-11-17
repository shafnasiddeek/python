from graphics import circle
from graphics import rectangle
from graphics.d_graphics import sphere
from graphics.d_graphics import cuboid

r=float(input("Enter Radius: "))
l=int(input("Enter Length of rectangle: "))
b=int(input("Enter Breadth of rectangle: "))
rs=int(input("Enter Radius Of Sphere: "))
lc=int(input("Enter Length of cuboid: "))
bc=int(input("Enter Breadth of cuboid: "))
h=int(input("Enter Height of cuboid: "))



print("Area: ",circle.area_of_circle(r))
print("The perimeter of circle is",circle.perimeter(r))
    
print("Area: ",rectangle.area_of_rectangle(l,b))
print("The perimeter of rectangle is",rectangle.rect_perimeter(l,b))

print("Area: ",sphere.spherv(rs))
print("The perimeter of sphere is",sphere.spherp(rs))

print("Area: ",cuboid.cuboida(lc,bc,h))
print("The perimeter of cuboid is",cuboid.cuboidp(lc,bc,h))
