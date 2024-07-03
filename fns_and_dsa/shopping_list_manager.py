def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))  # Convert input to an integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # Prompt for and add an item
            itemAdd = input("Enter the item to add: ").strip().lower()
            shopping_list.append(itemAdd)
        elif choice == 2:
            # Prompt for and remove an item
            itemRemove = input("Enter the item to be removed: ").strip().lower()
            if itemRemove in shopping_list:
                shopping_list.remove(itemRemove)
            else:
                print(f"Item '{itemRemove}' not found in the shopping list.")
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
