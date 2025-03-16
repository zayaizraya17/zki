import random
import string

def generate_password(length):
    # Алфавит
    alphabet = string.ascii_letters + string.digits
    # Генерируем
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

# прим
password = generate_password(6)
print("Сгенерированный пароль:", password)
