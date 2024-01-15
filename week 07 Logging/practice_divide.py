def divide_numbers():
    try:
        dividend = int(input("Enter the integer to divide: "))
        divisor = int(input("Enter the integer to divide by: "))
        return dividend / divisor
    except ValueError:
        print("Enter an integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print(type(e))
        print(e)


print(divide_numbers())
