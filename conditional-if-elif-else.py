# The elif keyword is Python's way of saying 
# "if the previous conditions were not true, 
# then try this condition".

a = 55
b = 50
if b > a:
  print('b is greater than a')
elif b < a:
  print('b is less than a')

c = 33
d = 33
if d > c:
  print('d is greater than c')
elif(c == d):
  print('c and d are equal')

# The "else" keyword catches 
# # anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# This technique is known as Ternary Operators, or Conditional Expressions.
# One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 