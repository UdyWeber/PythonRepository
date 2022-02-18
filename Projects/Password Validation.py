from getpass import getpass
import string

def validatePassword(password, confirmationPass):

    punctuation = string.punctuation
    upper_case = string.ascii_uppercase
    numbers = any(i.isdigit() for i in password)
    special_chars = [True for x in password if x in punctuation]
    upper_case_chars = [True for x in password if x in upper_case]
    
    if len(password) not in range(5, 21):
        return f"Passoword must be between 5 and 20 characters"

    if ' ' in password:
        return f"White space found in your password, please try again."

    if not numbers:
        return f"You should add at least 1 numeric character to your password."

    if not upper_case_chars:
        return f"You should have at least 1 Upper character in the password"

    if not special_chars:
        return f"You should have at least 1 special character into the password."

    if password == confirmationPass:
        
         if len(password) in range (5, 16): 
            return f"You have a medium security password \nYour password attend to all requisites and has been generated."
         elif len(password) not in range(17, 21):
            return f"You have a strong password \nYour password attend to all requisites and has been generated."
    else:
        return f"The passwords do not match, tryagain"

passwrd = getpass("Define a password please: ")
confirmPass = getpass("Confirm your password: ")

print(validatePassword(passwrd, confirmPass))