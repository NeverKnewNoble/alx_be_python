# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row
row = 0
while row < size:
    # Use a for loop to print asterisks side by side without advancing to a new line
    for col in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    row += 1
