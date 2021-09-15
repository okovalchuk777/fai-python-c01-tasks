time_in_sec = int(input("Enter time in seconds: "))
'''
How to pad a string with leading zeros in Python 3 [duplicate]
https://stackoverflow.com/questions/39402795/how-to-pad-a-string-with-leading-zeros-in-python-3/39402910
There are many ways to achieve this but the easiest way in Python 3.6+, in my opinion, is this:
print(f"{x:02}") - 00
print(f"{x:02}") - 000
'''
print(f'{time_in_sec // 3600:02}:{(time_in_sec - (time_in_sec // 3600 * 3600))//60:02}:{time_in_sec%60:02}')
