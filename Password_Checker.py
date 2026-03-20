import re

password = input("Enter your password: ")

length = len(password) >= 8
uppercase = re.search(r"[A-Z]", password)
lowercase = re.search(r"[a-z]", password)
digit = re.search(r"[0-9]", password)
special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

score = 0

if length:
    score += 1
if uppercase:
    score += 1
if lowercase:
    score += 1
if digit:
    score += 1
if special:
    score += 1

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Password Strength:", strength)

if not length:
    print("Suggestion: Use at least 8 characters")
if not uppercase:
    print("Suggestion: Add uppercase letters")
if not lowercase:
    print("Suggestion: Add lowercase letters")
if not digit:
    print("Sugeestion: Include numbers")
if not special:
    print("Suggestion: Include special characters")


common_passwords = ["123456", "password", "qwerty", "abc123", "admin"]

if password in common_passwords:
    print("This is a very common password! Choose a stronger one.")