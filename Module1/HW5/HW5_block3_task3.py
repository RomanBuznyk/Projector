#Write a function that implement case swapping. 
# It should return the same result as swapcase() method. 
# Your function should accept one str argument and convert 
# all lower case values to upper case and vice versa.

def swapcase(inp) -> str:
    for i in inp:
        if i.isupper():
            print(i.lower(), end = '')
        elif i.islower():
            print(i.upper(),  end = '')
    return ''  #для того щоб  None не було відразу після слова 
inp = input('Enter a word:')
print(swapcase(inp))
        

