import random

side1 = 0 #тут змінні для кожної сторони
side2 = 0
side3 = 0
side4 = 0
side5 = 0
side6 = 0
for i in range(1, 10000): #далі буде виконуватися цикл для кожної і 10000 раз
    dice = random.choice(range(1, 7))# зміннв для кубика яка дає цифру від 1 до 6 
    if dice == 1: # умова якщо випало 1 
        side1 += 1  # лічильник 
    elif dice == 2:
        side2 += 1
    elif dice == 3:
        side3 += 1
    elif dice == 4:
        side4 += 1
    elif dice == 5:
        side5 += 1
    elif dice == 6:
        side6 += 1
   
    
print('Side 1 appeard', side1, 'times  '\
    'Side 2 appeard', side2, 'times  '\
    'Side 3 appeard', side3, 'times  '\
    'Side 4 appeard', side4, 'times  '\
    'Side 5 appeard', side5, 'times  '\
    'Side 6 appeard', side6, 'times', sep = '\n')

