import subprocess
import time

# Запуск первой программы
try:
    subprocess.run(["python", "wert.py"], check=True)
    print("Первая программа завершена.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске программы 'wert.py': {e}")

# Пауза 15 секунд
print("Ждем 15 секунд перед запуском второй программы...")
time.sleep(15)

# Запуск второй программы
try:
    subprocess.run(["python", "country.py"], check=True)
    print("Вторая программа завершена.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске программы 'country.py': {e}")

# Пауза 15 секунд
print("Ждем 15 секунд перед запуском третьей программы...")
time.sleep(15)

# Запуск третьей программы
try:
    subprocess.run(["python", "number.py"], check=True)
    print("Третья программа завершена.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске программы 'number.py': {e}")

# Пауза 15 секунд
print("Ждем 15 секунд перед запуском четвертой программы...")
time.sleep(15)

# Запуск четвертой программы
try:
    subprocess.run(["python", "calc.py"], check=True)
    print("Четвертая программа завершена.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске программы 'calc.py': {e}")

# Пауза 15 секунд
print("Ждем 15 секунд перед запуском пятой программы...")
time.sleep(15)

# Запуск пятой программы
try:
    subprocess.run(["python", "calculator.py"], check=True)
    print("Пятая программа завершена.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске программы 'calculator.py': {e}")
