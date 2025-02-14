person = {}

i = 1
while True:
    x = input("Enter the name of the person: ")
    y = int(input("Enter the age of the person: "))
    z = input("Married or unmarried: ")

    person["p" + str(i)] = {
        "Name": x,
        "Age": y,
        "Status": z
    }

    print()
    i = i + 1
    m = input("Do you want to add more (y/n): ")
    if m == "n":
        break

print(person)

