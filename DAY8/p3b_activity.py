def get_dict_input(n):
    d = {}
    print(f"Enter {n} dictionary (key-value pairs):")
    while True:
        key = input("Enter key (or 'done' to finish): ")
        if key.lower() == 'done':
            print(f"{n} dictinary completed")
            print()
            break
        value = input("Enter value: ")
        d[key] = value
    return d

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Create a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] = [merged_dict[key], value]  # Handle overlapping keys
        else:
            merged_dict[key] = value
    return merged_dict

# Get user input
dict1 = get_dict_input("first")
dict2 = get_dict_input("second")

# Merge dictionaries
merged_dict = merge_dictionaries(dict1, dict2)

# Display result
print("Merged Dictionary:", merged_dict)
