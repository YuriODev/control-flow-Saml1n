<<<<<<< HEAD
# Input: A number (up to four digits)
number = int(input("Enter a number (up to 9999): "))

# Extract digits
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10

# Compare digits for uniqueness
is_unique = (thousands != hundreds or thousands == 0 or hundreds == 0) and \
            (thousands != tens or thousands == 0 or tens == 0) and \
            (thousands != ones or thousands == 0) and \
            (hundreds != tens or hundreds == 0 or tens == 0) and \
            (hundreds != ones or hundreds == 0) and \
            (tens != ones or tens == 0)

# Output the result
print(is_unique)
=======
# Your solution to Exercise 13

>>>>>>> e2be20ee77cdbae9a6d1e5effe3c3653928557aa
