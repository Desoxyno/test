import random
import string

random_letter = random.choice(string.ascii_letters)
random_digit = random.choice(string.digits)
random_special = random.choice(string.punctuation)

all_chars = string.ascii_letters + string.digits + string.punctuation
rest = ''.join(random.choice(all_chars) for _ in range(15)) 

password_list = list(random_letter + random_digit + random_special + rest)
random.shuffle(password_list)
password = ''.join(password_list)

print(password)