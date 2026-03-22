# Tysheena Mosley
# 03/21/2026
# Problem 3: Ask the user to enter numbers, store them in a list,
# and continue until the sum is greater than 100

# Create an empty list to store numbers
numbers = []

# Start the total at 0
total = 0

# Keep asking for numbers while the total is 100 or less
while total <= 100:
    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Add the number to the list
    numbers.append(num)

    # Add the number to the total
    total += num

# Print the list and the total
print("Numbers entered:", numbers)
print("Sum:", total)
