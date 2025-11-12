import string

password = input("Please enter your password: ")


upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])

charachters = upper_case + lower_case + digits + special

length = len(password)

score = 0

with open("common_passwords.txt", "r") as f:
    common_passwords = f.read().splitlines()

if password in common_passwords:
    print ("Password was found in common passwords list. Score: 0 / 100")
    exit()

if length >= 8:
    score += 1
if length >= 12:
    score += 1
if length >= 16:
    score += 1
if length >= 20:
    score += 1
print(f"Password length is {str(length)}, add {str(score)} points!")

if charachters > 1:
    score += 1
if charachters > 2:
    score += 1
if charachters > 3:
    score += 1
print(f"Password has {str(charachters)} different character types, adding {str(charachters -1)} points!")

if score < 4:
    print(f"Your password is very weak, please try again! Score: {str(score)} / 10")
elif score == 4:
    print(f"Your password is weak, try again! Score: {str(score)} / 10")
elif score == 5:
    print(f"Your password is moderately secure! Score: {str(score)} / 10")
elif score == 6:
    print(f"Your password is strong and secure! Score: {str(score)} / 10")

    