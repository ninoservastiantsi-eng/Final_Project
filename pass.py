import string

password = "hellonino"
upper_case = [1 if c in string.ascii_uppercase else 0 for c in password]
lower_case = [1 if c in string.ascii_lowercase else 0 for c in password]
digits = [1 if c in string.digits else 0 for c in password]
special_chars = [1 if c in string.punctuation else 0 for c in password]
amount_overall = sum(upper_case) + sum(lower_case) + sum(digits) + sum(special_chars)
print(string.ascii_uppercase)

print(upper_case)
print(upper_case.count(1))
print("Has uppercase letters" if upper_case.count(1) > 0 else "No uppercase letters")
