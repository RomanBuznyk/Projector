#1. All letters must be written in lowercase.
string_1 = "Animals  "
print(string_1.lower())



#2. All letters must be capitalized.

string_2 = "  Badger"
print(string_2.upper())


#3. Remove all spaces:

string_3 = "   HoneyPot   "

    #a) from the beginning of the line
print(string_3[3:])
    #b) from the end of the line
print(string_3[:11])
    #c) on both sides of the line
print(string_3[3:11])


#4. Check the value of the startwith ('Be') function for each line.:
string_1 = "Bear"
print(string_1.startswith('Be'))

string_2 = "bear"
string_2 = string_1.replace("b", "B")
print(string_2.startswith('Be'))


string_3 = "BEAR"
string_3 = "B" + (string_3[1:]).lower()
print(string_3.startswith('Be'))

string_4 = "bEar"
string_4 = string_4[0].upper() + string_4[1].lower() + string_4[2:4]
print(string_4.startswith('Be'))


#5. Find and replace all letters 's' with the letter 'x' in the following line: 

string = "Somebody said something to Samantha."
string = string.lower().replace("s", "x")
print(string)


#6. Leave only numbers in the following line using only string methods: 

string = '12345!,_6--'
string = string[0:5] + string[8]
print(string)


#7. (Optional) Find a secret message in the following text: `'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'` 
string = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'
string = string.replace("x", "")
string = string[::-1].replace("X", "")
print(string)
