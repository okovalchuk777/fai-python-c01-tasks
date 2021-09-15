start_distance = int(input("Enter the start distance in kilometers: "))
end_distance = int(input("Enter the end distance in kilometers: "))
intermediate_distance = start_distance
days = 1
while intermediate_distance // end_distance != 1:
    days += 1
    intermediate_distance = intermediate_distance * 1.1
    print(f'{days}th day: {intermediate_distance:.2f} kilometers.')
print(f'It will take {days} day(s) to reach the end distance - {end_distance} kilometers.')
