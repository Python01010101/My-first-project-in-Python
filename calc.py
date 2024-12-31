import os
os.system('cls' if os.name == 'nt' else 'clear')
number = int(input("Какую я число загадал "))
if 0 <= number <= 10:
    print("Я загадал легкое число")
elif 10 < number <= 25:
    print("Я загадал не сложное число")
elif 25 < number <= 1000:
    print("Я загодал сложное число")
else:
    print("Я загадал очень сложное число")