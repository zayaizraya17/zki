import random
import string

def generate_password(length):
    # Определение алфавита
    alphabet = string.ascii_letters + string.digits
    # Генерация пароля
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

# Пример использования
password = generate_password(6)
print("Сгенерированный пароль:", password)