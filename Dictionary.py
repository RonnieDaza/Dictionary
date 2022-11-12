# Menu
print("Menu:")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")

# Ask the user what to do.
choice = int(input("What do you want to do? (1-3) "))

if choice == 1:
    info = {"Jiya": "Caloocan"}
    
    name = input("Full Name: ")
    age = int(input("Age: "))
    address = input("Address: ")
    number = int(input("Phone Number: "))
    gender = input("Gender: ")
    country = input("Country: ")
    email = input("Email: ")
    info[name] = [age, address, number, gender, country, email]
    print(info)
