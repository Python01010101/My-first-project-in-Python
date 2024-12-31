# for i in range(100):
#    print("Привет мир")

# home = "Russia"
# if home == "USA":
#     print ("Hi Russia")
# else:
#         print ("Hi Zero")

import os
os.system('cls' if os.name == 'nt' else 'clear')



# age = int (input("Введите возраст: "))
# if age >= 18:
#     print("Вы совершенно летний.")
# else:
#     print("Вы несовершенно летний.")


#     if age < 12:
#         print ("Вы ребенок.")
#     elif age < 18:
#         print("Вы подросток. ")
#     else:
#         print("Вы взрослый.")


# num = int(input("Введите число: "))
# if num % 2 == 0 :
#     print("Число четное: ")
# else:
# #     print("Число не чётное: ")



# time = int(input("Введите время: "))

# if 0 <= time <= 11:  # Если время от 0 до 11
#     print("Сейчас утро!")
# elif 12 <= time <= 17:  # Если время от 12 до 17
#     print("Сейчас день!")
# elif 18 <= time <= 21:  # Если время от 18 до 21
#     print("Сейчас вечер!")
# else:  # Если время не попадает в эти диапазоны
#     print("Некорректное время!")



test  = int(input("Введите ваш набранный балл "))
if 0 <= test <= 50:
    print("Вы не прошли тест")
elif 50 <= test <= 69:
    print("Вы не плохо прошли тест")
elif 70 <= test <= 89:
    print("Вы хорошо прошли тест")
elif 90 <= test <= 100:
    print("Вы отлично прошли тест")
