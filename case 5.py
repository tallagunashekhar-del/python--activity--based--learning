

passwords = ["Hello@123", "password1", "abc", "Aaa111!!x", "Strong#Pass9"]
specials = "!@#$%^&*"
banned = ["password", "1234", "admin"]

for pwd in passwords:
    errors = []

    if len(pwd) < 8:
        errors.append("Less than 8 characters")

    has_upper = has_lower = has_digit = has_special = False
    for ch in pwd:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in specials:
            has_special = True

    if not has_upper:
        errors.append("No uppercase letter")
    if not has_lower:
        errors.append("No lowercase letter")
    if not has_digit:
        errors.append("No digit")
    if not has_special:
        errors.append("No special character")

    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i + 1] == pwd[i + 2]:
            errors.append("Same character repeated 3 times")
            break

    for word in banned:
        if word in pwd.lower():
            errors.append("Contains banned word: " + word)

    if len(errors) == 0:
        print(pwd, "-> VALID")
    else:
        print(pwd, "-> INVALID")
        for e in errors:
            print("    -", e)
