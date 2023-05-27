 # This program calculates the sum of all even numbers between 1 and a user-defined limit.

limit = int(input("Enter the limit: "))
sum_of_evens = 0

for num in range(1, limit + 1):
    if num % 2 == 0:
        sum_of_evens += num

print("The sum of even numbers from 1 to", limit, "is:", sum_of_evens)

