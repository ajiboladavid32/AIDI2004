def sum_of_even_numbers(limit):
    sum = 0
    for number in range(2, limit + 1, 2):
        sum += number
    return sum

# Getting user input for the limit
limit = int(input("Enter the limit: "))

# Calculating and printing the sum of even numbers
result = sum_of_even_numbers(limit)
print("The sum of even numbers between 1 and", limit, "is:", result)


