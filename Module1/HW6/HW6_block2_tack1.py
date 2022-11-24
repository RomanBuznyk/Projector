while True:
    try:
        number = int(input("Enter a number: "))
        print(number)
        break
    except ValueError:
        print("Not a number")

    


