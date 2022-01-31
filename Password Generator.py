import random
import string

print('Welcome to your password generator')

length = int(input('How many chracters in the password:'  ))

letter = string.ascii_letters 
num = string.digits

all = letter + num 

temp = random.sample(all, length)
password = ''.join(temp)

print('Behold your password is...  SAM' + password + "ZAC")
print('Use it wisely')