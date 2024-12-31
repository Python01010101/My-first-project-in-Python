import os
os.system('cls' if os.name == 'nt' else 'clear')



num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num2 != 0:
    remainder = num1 % num2
    print(f"Остаток от деления {num1} на {num2} равен {remainder}")
else:
    print("Деление на ноль невозможно!")
