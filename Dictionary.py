print("-----------------------------")
print("MENU:")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("-----------------------------")

info =  {"Mark": ["19", "Manila", "09123456789"]}

while True:

    choice = int(input("What do you want to do? (1-3) "))

    if choice == 1:
        fullName = input("Name: ")
        age = int(input("Age: "))
        address = input("Address: ")
        country = input("Country: ")
        phoneNumber = input("Phone Number: ")
        gender = input("Gender: ")
        email = input("Email: ")
        info[fullName] = [age, address, country, phoneNumber, gender, email]
        print("Saved!")
    
    elif choice == 2:
        askName = input("Enter the full name: ")
        print(info[askName])

        userData = {
            "Full Name": fullName,
            "Age": age,
            "Address": address,
            "Country": country,
            "Phone Number": phoneNumber,
            "Gender": gender,
            "Email": email
        }
    
    elif choice == 3:
        exit = input("Are you sure? (Yes/No) ")
        if exit == "Yes":
            break