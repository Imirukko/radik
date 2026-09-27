#task_3
import random
import string

password_list = (
    random.choices(string.ascii_uppercase, k=3) +
    random.choices(string.digits, k=3) +
    random.choices('!@#$%^&*', k=2)
)
random.shuffle(password_list)
password = ''.join(password_list)
print(password)
