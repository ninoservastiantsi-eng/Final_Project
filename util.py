import string

def check_password(password):
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])

    charachters = upper_case + lower_case + digits + special
    length = len(password)
    score = 0

    # common passwords
    with open("common_passwords.txt", "r") as f:
        common_passwords = f.read().splitlines()

    if password in common_passwords:
        return "Password was found in common passwords list, please try again. Score: 0 / 100"

    # length score
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if length >= 20:
        score += 1

    # char types score
    if charachters > 1:
        score += 1
    if charachters > 2:
        score += 1
    if charachters > 3:
        score += 1
    if charachters > 4:
        score += 1
    if charachters >= 5:
        score += 1

    # result text
    if score < 4:
        return f"Your password is very weak, please try again! Score: {score} / 7"
    elif score == 4:
        return f"Your password is weak, try again! Score: {score} / 7"
    elif score == 5:
        return f"Your password is moderately secure! Score: {score} / 7"
    elif score == 6:
        return f"Your password is strong and secure! Score: {score} / 7"
    elif score == 7:
        return f"Your password is extremely strong! Score: {score} / 7"
