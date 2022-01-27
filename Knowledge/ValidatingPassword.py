#Confirming Password
loop = True

while loop:
    password = input('Generate a Password: ')
    confirmedPassword = input('Confirm your Password: ')
    if password == confirmedPassword:
        print(f'You have succesfully generated the password!')
        break
    else:
        print(f'Try again, the passwords are different')

