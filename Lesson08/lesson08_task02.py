class MyOwnZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text


try:
    init_number01 = int(input("Enter the first number: "))
    init_number02 = int(input("Enter the second number: "))
    if init_number02 == 0:
        raise MyOwnZeroDivisionError("The second number should not be ZERO!!!")
    result = round(init_number01 / init_number02, 3)
except ValueError:
    print("You entered NOT a number!!!")
except MyOwnZeroDivisionError as err:
    print(err)
else:
    print(result)
