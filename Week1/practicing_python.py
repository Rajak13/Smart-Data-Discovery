#Type Conversion
#Coverting string to an integer and printing the sum.
a = 10
b = "20"
print(a + int(b))

#Some operators(_, -, *, /,//, %, **, and, or, not, ==, !=, >, <, >=, <=)
#Printing the result of the following operations.
print(10 + 20)
print(10 - 20)
print(10 * 20)
print(10 / 20)
print(10 // 20)
print(10 % 20)
print(10 ** 20)
print(10 and 20)
print(10 or 20)
print(not 10)
print(10 == 20)

#Control Flow
#if-else
num_1 = 10
num_2 = 20
if num_1>num_2:
    print(num_1 + num_2)
else:
    print(num_1 - num_2)

#for loop
for i in range(10):
    print(i)
    
#while loop
x = 0
while x <10:
    print(x)
    x +=1
    
#List Comprehension
squares = [x**2 for x in range(1, 9)]
print(squares)

