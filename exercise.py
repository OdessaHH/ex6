# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


#1
"""
three_mul = 'fizz' #1st bug, misses an '
five_mul = 'buzz'
num1 = 3
num2 = 5  #5th bug, 5 , not 4
max_num = 100
   
for i in range(1,max_num): #4th bug, max_num , not max_number #6 bug, 1, not i
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0 and i%num2 == 0: #6th bug, wrong order in the code, 7th bug change statement
        print(i,three_mul+five_mul) #3rd bug, misses a tab
    elif i%num1 == 0: #2nd bug, misses an =
        print(i,three_mul)
    elif i%num2 == 0:
        print(i,five_mul)
    

    #elif i%num1 == 0 and i%num2 == 0: 
     #   print(three_mul+five_mul) #3rd bug, misses a tab
   
# maybe just 6 bugs
"""
2#
"""
n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number # bug sum + number, not sum + 1
    number = number + 1

    #number = number + 1
print("Sum =", sum)
"""



#3
"""
n = 5
sum = 0
for num in range(n+1): #bug, misses n+1
    sum += num
print("Sum =", sum)
"""



4#
"""
for x in range(3): #bug, misses an :
    print(x)
"""

"""
for j in range(5):
    print("This is loop number ", j) # bug, misses an ",j"
"""


"""
x = 10  # bug, wrong order 
while x > 0:
    print(x)
    x -= 1
    
"""


"""

countdown = 5 #bug, 5, not 10
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")
"""


#5
"""
x = int(input("First number: ")) #4th bug, misses an int()
y = int(input("Second number: "))
z = int(input("Third number: ")) #1st bug, too much )

if x == y or y == z or x == z: #2nd bug, misses x==z ;3rd bug  ==, not =
    print("Calculated sum is 0")
    #result = 0
else:
    
    print("Calculated sum is ", x + y + z)
"""


6#

"""
x = int(input("First number: ")) #1st bug, misses int()
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20: #2nd bug, and, not or 5#th bug  >=, not >
    sum = 20
    print("Calculated sum is ", sum) #3rd bug
else:
    print("Calculated sum is ",result) #4th bug


"""
7#
"""
a = input("First value: ") #1st bug, misses an input()
b = input("Second value: ")

print("Before swapping: a =", a, ", b = ", b) #2nd bug, misspelling of output

temp = a
a = b

b = temp #3rd bug, fix
print("After swapping: a =", a, " ,b =", b)

"""

#8
"""
x = float(input("First number: ")) #1st bug =, not ==
y = float(input("Second number: "))
z = float(input("Third number: "))

xyz = [x,y,z] #3rd fix, creating a list and using max() and min()
print("The maximum value is ", max(xyz))
print("The minimum value is ", min(xyz)) # 2nd bug, abs() is unnecessary
"""


9#


"""
x = input("Type your value: ") #1st bug

if x == "0": #2nd bug ==, not 0, 3rd fix. just use a string
    x = False
elif x == "1":
    x = True
else:
    pass #tab missing

print("Your entered value is now ", x)
   
   
"""
"""
#10
x = int(input("First number: ")) #1st bud, int() missing
y = int(input("Second number: "))

if x % y == 0: #2nd bug %, not %% #3rd bug ==, not <=
    print("First number is divisible by second number, result =", x / y)
elif y % x == 0: #4th bug ==, not !=
    print("Second number is divisible by first number, result =", y / x) #5th bug /, not //
else:
    print("Numbers are non-divisible!") #6th misspelling

"""
