import random 
from random import choice


capitals = { 'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome', 'USA': 'Washington',\
    'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna', 'Belgium': 'Brussels', 'Sweden': 'Stockholm',\
    'Norway': 'Oslo', 'Denmark': 'Copenhagen', 'Finland': 'Helsinki',  'Poland': 'Warsaw', \
    'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'}


#countries = list(capitals.keys())

while True
        country_choice = random.choice(list(capitals.keys()))
        capital = capitals[country_choice]
        print(f' The country is', country_choice)
        answer = input('What is the capital of given country?')
        score = 0
        if answer == 'Exit':
            break
        elif answer == capital:
            score += 1
            print('Correct.\n Score is %d \n Quize goes on. \n If you wnat to quit - write Exit' %score)
            
        elif answer != capital:
            print('Wrong, please try again.  \n If you wnat to quit - write Exit')

