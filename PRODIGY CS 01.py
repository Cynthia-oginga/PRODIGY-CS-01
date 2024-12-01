import re

def check_password_strength(password):
    # Initialize the feedback messages
    feedback = []
    
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")
    
    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        feedback.append("Password must contain at least one lowercase letter.")
    
    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        feedback.append("Password must contain at least one uppercase letter.")
    
    # Check if the password contains at least one digit
    if not re.search(r'[0-9]', password):
        feedback.append("Password must contain at least one digit.")
    
    # Check if the password contains at least one special character
    if not re.search(r'[\W_]', password):
        feedback.append("Password must contain at least one special character (e.g., !, @, #).")
    
    # Provide feedback based on the password's strength
    if not feedback:
        return "Password is strong!"
    else:
        return "\n".join(feedback)

# Input from the user
password = input("Enter your password: ")
result = check_password_strength(password)

# Display the result
print(result)
