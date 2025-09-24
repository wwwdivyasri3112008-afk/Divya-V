import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) < 8:
        remarks.append("Too short (minimum 8 characters).")
    else:
        strength += 1

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("Add lowercase letters.")
    
    if re.search(r'\d', password):
        strength += 1
    else:
        remarks.append("Add digits.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        remarks.append("Add special characters.")

    common_passwords = ['password', '123456', 'qwerty', 'admin']
    if password.lower() in common_passwords:
        remarks.append("Avoid common passwords.")
        
    if strength >= 4:
        verdict = "Strong"
    elif strength == 3:
        verdict = "Moderate"
    else:
        verdict = "Weak"

    return verdict, remarks

pwd = input("Enter your password: ")
verdict, feedback = check_password_strength(pwd)
print(f"Password Strength: {verdict}")
if feedback:
    print("Suggestions:")
    for item in feedback:
        print(f"- {item}")
