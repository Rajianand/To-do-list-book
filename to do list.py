# Function to display the to-do list
def display_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for idx, item in enumerate(todo_list, start=1):
            print(f"{idx}. {item}")

# Function to add an item to the to-do list
def add_item(todo_list, item):
    todo_list.append(item)
    print(f"Added '{item}' to your to-do list!")

# Function to remove an item from the to-do list
def remove_item(todo_list, index):
    if 1 <= index <= len(todo_list):
        removed_item = todo_list.pop(index - 1)
        print(f"Removed '{removed_item}' from your to-do list!")
    else:
        print("Invalid index. Please enter a valid index.")

# Example usage:

# Initialize an empty to-do list
to_do_list = []

while True:
    print("\nWhat would you like to do?")
    print("1. Display to-do list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_list(to_do_list)
    elif choice == '2':
        new_item = input("Enter the item you want to add: ")
        add_item(to_do_list, new_item)
    elif choice == '3':
        display_list(to_do_list)
        if to_do_list:
            index_to_remove = int(input("Enter the index of the item to remove: "))
            remove_item(to_do_list, index_to_remove)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
