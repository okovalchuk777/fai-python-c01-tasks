class MyOwnNotaNumberError(Exception):
    def __init__(self, text):
        self.text = text


init_number = 'start'
init_number_list = []
while init_number != 'quit':
    try:
        init_number = str(input("Enter the number (if You want to STOP enter word quit): "))
        if init_number.isdigit():
            init_number_list.append(init_number)
        else:
            raise MyOwnNotaNumberError("Entered value is NOT a number!!!")
    except MyOwnNotaNumberError as err:
        print(err)

print(init_number_list)
