import random


# Line 1
print(random.randint(5, 20))
# What did you see on line 1?
# I see random integers like 11, 17, or 20, depending on execution.

# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, Largest: 20

# Line 2
print(random.randrange(3, 10, 2))
# What did you see on line 2?
# I see random integers like 3, 5, 7, or 9, depending on execution.

# What was the smallest number you could have seen, what was the largest?
#Smallest: 3, Largest: 9

# Could line 2 have produced a 4?
#No, because the step is 2, so only 3, 5, 7, and 9 are valid results.

# Line 3
print(random.uniform(2.5, 5.5))
# What did you see on line 3?
# I see random floating-point numbers like 3.863402814809395 number that is between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5, Largest: 5.5
# Write code, not a comment, to produce a random number between 1 and 100 inclusive:
print(random.randint(1, 100))