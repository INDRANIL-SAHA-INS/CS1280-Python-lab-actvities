def list_operations():
    my_list = [2,4,68,11,3]

    while True:
        print("\nList Operations:")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Find an element")
        print("4. Display list")
        print("5. Sorting")
        print("6.Reversing")
        print("7.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter element to insert: ")
            my_list.append(element)
            print(f"Element '{element}' inserted.")

        elif choice == 2:
            element = input("Enter element to delete: ")
            if element in my_list:
                my_list.remove(element)
                print(f"Element '{element}' deleted.")
            else:
                print(f"Element '{element}' not found.")

        elif choice == 3:
            element = int(input("Enter element to find: "))
            if element in my_list:
                print(f"Element '{element}' found.")
            else:
                print(f"Element '{element}' not found.")

        elif choice == 4:
            print("Current List:", my_list)
        
        elif choice == 5:
            my_list.sort()
            print("Current List:", my_list)
            
        elif choice ==6:
            my_list.reverse()
            print("Current List:", my_list)
            
            
        

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

# Call the function to start the program
list_operations()
