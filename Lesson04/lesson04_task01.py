from sys import argv

try:
    script_name, output_per_hour, rate_per_hour, bonus = argv
    salary = (round(abs(float(output_per_hour)) * abs(float(rate_per_hour)) + abs(float(bonus)), 2))
except ValueError:
    print(f'Three parameters (only numbers) must be entered.')
else:
    print(salary)
