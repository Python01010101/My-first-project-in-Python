import os
os.system('cls' if os.name == 'nt' else 'clear')


num = int(input("Введите число: "))
if 0 < num < 10:
    print("Cood work")
elif 10 <= num <= 100:
    print("Great work")