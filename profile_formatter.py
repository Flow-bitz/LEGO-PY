first_name = 'Eze'
last_name = 'Miracle'
country = 'Nigeria'
email = 'ezeonyekachi@gmail.com' 
full_name = first_name  + ' ' +last_name
email_domain = email.split('@')[1]

print('PERSONAL PROFILE')
print('------------------')
print()
print('Full name:', full_name)
print('Uppercase:', full_name.upper())
print('Lowercase:', full_name.lower())
print('Country:', country)
print('Email:', email)
print()
print('Username:', first_name)
print('Email domain:',email_domain)
print()
print(full_name.__len__())