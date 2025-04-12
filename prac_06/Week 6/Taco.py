
"""
Write a User class, for a fun Taco Reward program
A User know: name, number of tacos,(start at 5, goes
down when they give a taco) and their score
A User can give a taco to another user
We should be able to print a User like:
    Ben, 2 point, 4 tacos left
When we make a user, they start with the name we want
and appropriate default values
"""

class User:
    def __init__(self, name):
        self.name = name
        self.tacos = 5
        self.score = 0

    def give_taco(self, other_user):
        """Give a taco to another user and update scores."""
        if self.tacos > 0:
            self.tacos -= 1
            other_user.score += 1
            print(f"{self.name} gave a taco to {other_user.name}!")
        else:
            print(f"{self.name} has no tacos left to give!")

    def __str__(self):
        return f"{self.name}, {self.score} point(s), {self.tacos} tacos left"

# Example usage
user1 = User("Ben")
user2 = User("Alice")

print(user1)  # Ben, 0 point(s), 5 tacos left
user1.give_taco(user2)
print(user1)  # Ben, 0 point(s), 4 tacos left
print(user2)  # Alice, 1 point(s), 5 tacos left
