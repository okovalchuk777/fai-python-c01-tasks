def func_data_collection(firstname, lastname, year_of_birth, city_of_residence, email, phone):
    return print(f"{firstname} {lastname}, year of birth: {year_of_birth}, city_of_residence: {city_of_residence}, "
                 f"email: {email}, phone: {phone}.")


firstname01 = input("Enter your firstname: ")
lastname01 = input("Enter your lastname: ")
year_of_birth01 = int(input("Enter your year of birth: "))
city_of_residence01 = input("Enter your city of residence: ")
email01 = input("Enter your email: ")
phone01 = input("Enter your phone: ")

func_data_collection(phone=phone01, email=email01, city_of_residence=city_of_residence01, year_of_birth=year_of_birth01,
                     lastname=lastname01, firstname=firstname01)
