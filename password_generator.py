#Password Generator
#Write a programme, which generates a random password for the user. 
#Ask the user how long they want their password to be, and how many letters and numbers they want in their password. 
#Have a mix of upper and lowercase letters, as well as numbers and symbols. 
#The password should be a minimum of 6 characters long.

import random
import string

letters_of_password = int(input('Enter Number of letters of password: '))
numbers_of_password = int(input('Enter Number of numbers of password: '))

number_list =  ''.join(random.choice(string.digits) for i in range(numbers_of_password))
letter_list = ''.join(random.choice(string.ascii_letters) for i in range(letters_of_password))
	
syntax_list = number_list + letter_list + '!@#'
if len(syntax_list) < 6:
    print('Password should be minimum 6 characters')
    exit()
result = random.sample(syntax_list, len(syntax_list)) 
password = ''.join((result))
print('Your pasword is {}'.format(password))
