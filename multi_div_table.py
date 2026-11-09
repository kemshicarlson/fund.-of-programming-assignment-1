print("Welcome to the Table Generator")

# ask the user for the number and how far the table should go
number = int(input("Enter the number you want a table for: "))
limit = int(input("How far should the table go? (e.g. 10 or 12): "))

# ask which table the user wants
print("Which table do you want?")
print("1. Multiplication")
print("2. Division")
print("3. Both")
choice = input("Enter 1, 2 or 3: ")

# multiplication table
if choice == "1" or choice == "3":
    print("\nMultiplication table for", number)
    print("-------------------------")
    for i in range(1, limit + 1):
        answer = number * i
        print(number, "x", i, "=", answer)

# division table
# we divide the answers of the multiplication by the number
# so that the results are always whole numbers
if choice == "2" or choice == "3":
    print("\nDivision table for", number)
    print("-------------------------")
    for i in range(1, limit + 1):
        product = number * i
        answer = product // number
        print(product, "/", number, "=", answer)

if choice != "1" and choice != "2" and choice != "3":
    print("Invalid choice, please run the program again")

print("\nThank you for using the Table Generator")