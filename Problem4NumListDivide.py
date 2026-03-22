# Tysheena Mosley
# 03/21/2026
# Problem 4: Create a while loop from 0 to 50.
# If a number is divisible by 10, add it to the list called tens.

# Create an empty list
tens = []

# Start the counter at 0
counter = 0

# Keep looping until counter reaches 50
while counter <= 50:
    # Check if the number is divisible by 10
    if counter % 10 == 0:
        tens.append(counter)

    # Increase the counter by 1
    counter += 1

# Print the results
print(tens)
