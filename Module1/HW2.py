#Теорія
#1. Наведіть програмний приклад логічної та синтаксичної помилки.
'''
Logic error:

a = ('Tom')
b = ('Jerry')
print(a +  'and' + b)

Will return TomJerry 
so wee need to put space in the end of Tom and And
'''

'''
Syntax error:
a = ('Tom')
b = ('Jerry')
print(a + and + b)

We need to do like this 'and'
'''


#2. Який буде результат при 1 / 0, 0 / 1 - зафіксувати його та пояснити.
'''
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
'''
'''
>>> 0 / 1
0.0
'''

#3. Навіщо потрібні коментарі ?
#Коменарі потрібні щоб пояснити шось не торкаючись самого коду.

#4. Що таке змінна ?
#Змінна це частина памʼяті, яка мая імʼя

#Практика
#1. Написати програму яка отримує від користувача два числа. Вивести ці два числа в консоль
'''
a = input('Enter digit or number:')
b = input('Enter digit or number:')
print(a, b)
'''
#2. Провести та вивезти над ними всі базові арифметичні операції в print
'''
a = int(input('Enter digit or number:'))
b = int(input('Enter digit or number:'))
print(a, b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
'''

#3. Додати функціонал по знаходженню степені числа. Перше число є базою, друге - ступенем.
    #Вивести результат в консоль у форматі "а в b степені це c»
'''
a = int(input('Enter digit or number:'))
b = int(input('Enter digit or number:'))
print(a, b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
c = a ** b
print("a в b степені це", c)
'''
#4. Додати можливість працювати зі float
'''
a = float(input('Enter digit or number:'))
b = float(input('Enter digit or number:'))
print(a, b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
c = a ** b
print("a в b степені це", c)
'''
#5. Прийняти від користувача ім'я, призвіще, вік, вивезти одним print:
    #Name Surname
    #You are, вік , years old
'''
name = input('Name?')
surname = input('Surmane?')
age = input('Age?')
print(' ' + name + ' ' + surname, '\n', 'You are,' + age  + 'years old')
'''

