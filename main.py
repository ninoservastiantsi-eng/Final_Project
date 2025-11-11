import string

password = "helloWorld"

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
    print ("password is too common and insecure. Score: 0 / 7")
    exit()

if length >= 8:
    score += 1
if length >= 12:
    score += 1
if length >= 16:
    score += 1
if length >= 20:
    score += 1