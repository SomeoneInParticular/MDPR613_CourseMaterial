# Greet the user
print("Hello!")

# Initiate a list to track the all collected values
tracked_values = []

# Initiate a variable to track the absolute sum of said prior values
abs_sum = 0

# Loop until the absolute sum exceeds 100
while abs_sum <= 100:

    # Request a number from the user
    new_val = input("Please enter a number. Enter 'done' if you do not want to submit any further values: ")
    
    # If they type "done", break early
    if new_val == "done":
        break
    # To avoid redundancy, format the value explicitly as a float if the prior check failed
    else:
        new_val = float(new_val)
    
    # Otherwise, append the number onto our list of tracked values
    tracked_values.append(new_val)
    
    # Check if the number is negative, and make it positive if it is
    if new_val < 0:
        new_val *= -1
        
    # Add the (now absolute) value to our absolute sum, declared prior
    abs_sum += new_val
    
    
# Declare a new variable, this time for the cummulative product
cum_prod = 1
    
# For each element in the list, do the following:
for val in tracked_values:

    # Add 2 to the value, and print out the result
    print(f"Number plus two: {val+2}")
    
    # Multiply the new value into the cumulative product, printing out the result
    cum_prod *= val
    print(f"Cummulative product: {cum_prod}")
