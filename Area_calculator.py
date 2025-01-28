def area_calculator(shape):
 match shape:
  case 1:
   return "Triangle"
  case 2:
   return "Rectangle"
  case 3:
   return "Square"
  case 4:
   return "Circle"
  case 5:
   return "Exit"
  
shape = int(input("Enter the shape number (1-5): "))

if shape == 1:
 b = float(input('Enter the base of a triangle:'))
 h = float(input('Enter the height of triangle:'))
 area = 0.5*b*h
 print("The area of triangle is", area)
elif shape == 2:
 length = int(input('Enter the length of rectangle:'))
 width = int(input('Enter the width of rectangle:'))
 area = length*width
 print("The area of rectangle is", area)
elif shape == 3:
 side = int(input('Enter the length of a side of square:'))
 area = side **2
 print("The area of square is", area)
elif shape == 4:
 radius = float(input('Enter the radius of a circle:'))
 area = 3.14* radius **2
 print("The area of circle is", area)
else:
 print('Exiting the program')
 