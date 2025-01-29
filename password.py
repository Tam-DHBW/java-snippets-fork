import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_password(12))  # Example Output: 'aB3$dE5&fG1!'
asdfasdfasdf