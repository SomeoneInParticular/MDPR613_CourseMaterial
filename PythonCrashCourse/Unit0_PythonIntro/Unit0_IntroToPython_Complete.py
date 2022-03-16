# Greet the user
print("Welcome to MathDemo.py")

# Request the user's name, stored for later in a variable
user_name = input("Please enter your name: ")

# Request two numbers from the user (converted to integer form)
a = int(input("Please enter an integer (a): "))
b = int(input("Please enter another number (b): "))

# Compare the two numbers, saving the result to a variable for later
compared_result = a > b

# Report whether the first number is greater than the second
print("Is a greater than b? " + str(compared_result))

# Calculate and report the sum of the two numbers
sum_val = a + b
sum_str = str(a) + " plus " + str(b) + " equals " + str(sum_val)
print(sum_str)

# Calculate and report the difference between the two numbers
dif_val = a - b
dif_str = f"{a} subtract {b} equals {dif_val}"
print(dif_str)

# Calculate and report the product of the two numbers
prod_val = a * b
print(f"{a} times {b} equals {prod_val}")

# Calculate and report the ratio along with its remainder (remember floor division!)
print(f"{a} divide by {b} equals {a // b} remainder {a % b}")

# Say farwell to the user by name
print("Goodbye " + user_name)
