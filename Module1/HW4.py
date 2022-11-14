

'''
#Practice section 1

#Figure out the result of the following expressions:

#a) (1 <= 1) and (1 != 1)
False
#b) not (1 != 2)
False
#c) ("good" != "bad") or False
True
#d) ("good" != "Good") and not (1 == 1)
False

#Make all of them True by adding parentheses:

#a) False == (not True)

#b) (True and False) == (True and False)

#c) not (True and "A" == "B")
'''

#Practice section 2
#1. Write a Python program that reads two integers representing a month and prints the season for that month. Get month from the user input.

    #Expected Output:

    #Input the month: october

    #Season is autumn
'''
month = int(input('Enter the month:'))
if month == 1:
    print("Jenuary")
    print('Season in Winter')
elif month == 2:
    print('February')
    print('Season in Winter')
elif month == 3:
    print('March')
    print('Season is Spring')
elif month ==  4:
    print('April')
    print('Seaon is Spring')
elif month == 5:
    print('May')
    print('Season is Spring')
elif month == 6:
    print('June')
    print('Season is Summer')
elif month == 7:
    print('July')
    print('Season is Summer')
elif month == 8:
    print('August')
    print('Season is Summer')
elif month == 9:
    print('September')
    print('Season is Autumn')
elif month == 10:
    print('October')
    print('Season is Autumn')
elif month == 11:
    print('November')
    print('Season is Autumn')
elif month == 12:
    print('December')
    print('Season in Winter')
else:
    print("Must be a number 1-12")
'''


#2. Write a Python program to get next day of a given date. Get day, month and year from the user input.

    #Expected Output:

        #**Input a year:** 2022                                                     
        #**Input a month [1-12]:** 8                                               
        #**Input a day [1-31]:** 23                                           
        #The next date is [yyyy-mm-dd] 2022-8-24
'''
year = int(input('Enter year:'))
month = int(input('Enter month:'))
day = int(input('Enter day:'))
print(year, month, day, sep='\n')

if  1 <= day < 31:
    day +=1
    print('The next date is:', year, '-', month, '-', day)
elif 1 <= month < 12:
    print('The next date is:', year, '-', month, '-', day)
elif month == 12:
    month = 1
    year += 1
    print('The next date is:', year, '-', month, '-', day)
else:
    day = 1
    print('The next date is:', year, '-', month, '-', day)
'''



#3. Get a phrase from user input. Display whether the lenght of the string if longer than 5 characters, equal to 5 characters or shorter than 5 characters. Use if, elif, else for this.
'''
phrase = (input('Wright something:'))
if len(phrase) < 5:
    print('Less than 5')
elif len(phrase) == 5:
    print('5 exactly')
else:
    print('More than 5')
'''

#4. Get a positive number from user input. Find all factors of this number.

    #Example:

        #If the number is 6, the factors are: 1, 2, 3, 6
        #If the number is 10, the factors are: 1, 2, 5, 10
'''
number = int(input('Enter the number:'))
for i in range (1, number + 1):
  if (number % i == 0 ):
    print(i, end=',')
'''
#5. Write a Python program to check a triangle is equilateral, isosceles or scalene. Get all three sides from user input.

#Note :

    #An equilateral triangle is a triangle in which all three sides are equal.
    #A scalene triangle is a triangle that has three unequal sides.
    #An isosceles triangle is a triangle with (at least) two equal sides.
'''
side_1 = int(input('Enter side 1:'))
side_2 = int(input('Enter side 2:'))
side_3 = int(input('Enter side 3:'))
if side_1 == side_2 == side_3:
    print('Triangle is equilateral')
elif side_1 == side_2 or side_1 == side_3:
    print('Triangle is isosceles')
else:
    print('Triangle is scalene')
'''

#Practice section 3:
#1. Write a for loop that prints out the integers from 2 to 10, each on a new line, by using the range() function.
'''
for i in range(2, 11):
    print(i)
'''
#2. Use a while loop that prints out the integers from 2 to 10
'''
integer  = 2
while 2 <=  integer <=10:
    print(integer)
    integer += 1
print()
'''
#3. Write a program that takes number as its input and doubles that number few times in a loop. 
# Number of iterations and initial number should be taken from user input. 
# You should display each result on a separate line. Here is some sample output:

#Input:
#initial number: 2
#number of iterations: 5

#Output:
#4
#8
#16
#32
#64
'''
number_1 = int(input('Enter number:'))
iteration = int(input('Enter number 0f iterations:'))
for i in range(iteration):
    number_1 *= 2
    print(number_1)
'''

#4. Write a program that caluculate Fibonacci series. The Fibonacci series is a series of numbers in which each number is the sum 
# of the two preceding numbers. The first two numbers are 1 and 1. The third number is 1 + 1 = 2, 
# the fourth number is 1 + 2 = 3, and so on. Number of iterations should be taken from user input.
'''
iteration = int(input('Enter a number:'))
first = 1
second = 1
all = 0
while all < iteration:
    print(first)
    fib = first + second
    first = second
    second = fib
    all += 1

'''

#5. Write a program that takes a number as input and revert it using math operators.
#  You might use result of the exercise from the first lesson. 
# Here you should be able to do it not only for three-digit numbers, but for any numbers.
'''
numbers = input('number:')
print(numbers)
print(numbers[::-1])
'''

#Practice section 4
#1. Write a program that always asks user to input somethings. Quit only if user inputs 'q' or 'Q'.
'''
while True:
    inp = input('Enter somthing:')
    if inp != 'Q' or 'q':
        continue   
    elif inp == 'q' or inp == 'Q':
        break
    print('stop')
''' 
#2. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.
'''
for i in range(0, 100):
    if i % 3 == 0:
        print(i, end= ' ,')
'''

#3. Get a number from user input and iterate from 0 to that number.

    #A. Print 'foo' if the number is divisible by 3.
    #B. Print 'bar' if the number is divisible by 5.
    #C. Print 'foobar' if the number is divisible by both 3 and 5.

'''
inp = int(input('Enter number:'))
for i in range(0, inp):
    if i % 3 == 0:
        print('foo')
    elif i % 5 == 0:
        print('bar')
    elif i % 3 and i % 5 == 0:
        print('foobar')
'''
