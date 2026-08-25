import math
import random
#types

x = 5
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

x1 = "24"
print(type(x1))
x1 = int(x1)
print(type(x1 * 3))

y1 = 3 #real
z1 = 4 #imaginary
print(complex(y1,z1))

#Operator
print(2+3)
print(4-2)
print(4*3)
print(7/2)
print(7 // 2)
print(9 % 2)
print(2 ** 3)

x2 = 3
#x2 = x2 + 3
print(x2)
x2 += 3
print(x2)

#Rounding
print(2-10)
print(abs(2-10))

price = 334.344443
print(int(price))
print(round(price))
print(round(price,2))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))

#Advanced Maths
x3 = 4
print(math.sqrt(x3))

print(random.random())
print(random.randint(1,6))

rand_num = random.randint(1,100)
if(rand_num % 2 == 0):
    print("Even Number", rand_num)
else:
    print("Odd Number", rand_num)