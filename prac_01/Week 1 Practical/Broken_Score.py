"""
CP1404/CP5632 - Practical
Broken program to determine score status


# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")
"""

"""
fixed_score.py - corrected score checker

Rules:
 - score must be between 0 and 100 inclusive
 - 90 or more -> Excellent
 - 50 or more -> Passable
 - below 50 -> Bad
"""

def classify_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    score = float(input("Enter score: "))
    print(classify_score(score))
