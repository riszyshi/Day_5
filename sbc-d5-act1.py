num = []  # Initialize an empty list

num_range = int(input("Enter a number: "))
for i in range(1, num_range + 1):
    num.append(i)

while True:  
    print(num)  # Print the current list
    Boss_Stat = input("Is the boss there? Type Y/N: ").upper()  # Ask if the boss is present
    if Boss_Stat in ["Y", "N"]:  # Check if input is 'Y' or 'N'
        option = input("Choose ADD/REMOVE or type EXIT to stop: ").upper()  # Get the user's action
        if option == "ADD":
            add_num = int(input("Enter number to add: "))  # Get a number to add
            num.insert(0, add_num) if Boss_Stat == "N" else num.append(add_num)   # Add number based on Boss_Stat
        elif option == "REMOVE":
            if num:  # Check if the list is not empty
                num.pop(-1) if Boss_Stat == "N" else num.pop(0)  # Remove number based on Boss_Stat
            else:
                print("No elements to remove.")  # Inform if the list is empty
        elif option == "EXIT":
            break  # Exit the loop
        else:
            print("Type ADD/REMOVE/EXIT ONLY.")  # Prompt for valid input
    else:
        print("Y/N LANG ANG QUESTION OY!")  # Prompt for 'Y' or 'N'