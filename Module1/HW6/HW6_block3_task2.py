import random

numbersbank = list(range(1, 10000))
dice = random.choice(numbersbank)
for i in numbersbank:
    if dice == 1:
        print(f'1 occured "i" times')
    
