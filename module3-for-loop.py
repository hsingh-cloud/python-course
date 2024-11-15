# https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/
# inputs
a = 13
b = 5

c = a % b
print(a, "mod", b, "=",
      c, sep=" ")

# sequence type in python

for letter in 'hello!':
    print('Current letter:', letter)

for counter in range(1,11):
    print(counter)
print('Finished!')

for counter in range(1,11,2):
    print(counter)
print('Finished!')

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
