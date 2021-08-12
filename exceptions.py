import sys
try:
    x= int(input("x: "))
    y= int(input("y: "))
except ValueError:
    print("Error :Cannot Divide by non number .")
    sys.exit(1)

try:
    result= x/y
except ZeroDivisionError:
    print("Error :Cannot Divide by 0.")
    sys.exit(1)


print(f" result is  {result}")
