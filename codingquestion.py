# Functions for Lists
def list_operations():
    print("\nList Operations:")
    my_list = list(map(int, input("Enter list elements separated by space: ").split()))
    print(f"Original List: {my_list}")

    # Append
    element = int(input("Enter an element to append to the list: "))
    my_list.append(element)
    print(f"After Append: {my_list}")

    # Reverse
    my_list.reverse()
    print(f"After Reverse: {my_list}")

    # Delete
    del my_list
    print("List Deleted")

# Functions for Dictionaries
def dict_operations():
    print("\nDictionary Operations:")
    my_dict = {}
    n = int(input("Enter number of elements in the dictionary: "))
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value
    print(f"Original Dictionary: {my_dict}")

    # Append (Add a new key-value pair)
    key = input("Enter a key to append: ")
    value = input("Enter a value to append: ")
    my_dict[key] = value
    print(f"After Append: {my_dict}")

    # Reverse (not directly possible, but we can reverse the order of items)
    reversed_dict = {k: my_dict[k] for k in reversed(my_dict)}
    print(f"After Reverse: {reversed_dict}")

    # Delete
    del my_dict
    print("Dictionary Deleted")

# Functions for Sets
def set_operations():
    print("\nSet Operations:")
    my_set = set(map(int, input("Enter set elements separated by space: ").split()))
    print(f"Original Set: {my_set}")

    # Append (Add an element)
    element = int(input("Enter an element to add to the set: "))
    my_set.add(element)
    print(f"After Append: {my_set}")

    # Reverse (not directly possible since sets are unordered)
    print("Reverse not applicable for sets (unordered collection)")

    # Delete
    del my_set
    print("Set Deleted")

# Functions for Tuples
def tuple_operations():
    print("\nTuple Operations:")
    my_tuple = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
    print(f"Original Tuple: {my_tuple}")

    # Append (create a new tuple with an additional element)
    element = int(input("Enter an element to append to the tuple: "))
    my_tuple = my_tuple + (element,)
    print(f"After Append: {my_tuple}")

    # Reverse (create a new tuple with reversed elements)
    reversed_tuple = my_tuple[::-1]
    print(f"After Reverse: {reversed_tuple}")

    # Delete
    del my_tuple
    print("Tuple Deleted")

# Main function to run all operations
def main():
    list_operations()
    dict_operations()
    set_operations()
    tuple_operations()

if __name__ == "__main__":
    main()
