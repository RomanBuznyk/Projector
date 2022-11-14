#Write a program called convert_cel_to_fahr() that takes a temperature in Celsius and
#returns the equivalent temperature in Fahrenheit. 
# It should take a number as an argument from user input and return a number to the console.

def convert_cel_to_fahr(x) -> int:
    fahrenheit = (x * (9 / 5)) + 32
    return (fahrenheit)
x = int(input("Enter Celius:"))
print(f'Fahrenheit is', convert_cel_to_fahr(x))