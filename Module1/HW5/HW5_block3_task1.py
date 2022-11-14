#Write a function called square() with one argument of int type 
# and returns the value of that number raised to the second power.

def square(inp) -> int:
    return inp ** 2
inp = int(input('Enter a number:'))
print(square(inp), 'is a square of', inp)