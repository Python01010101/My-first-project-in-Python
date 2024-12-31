import os
os.system('cls' if os.name == 'nt' else 'clear')

test  = int(input("Введите ваш набранный балл "))
if 0 <= test <= 50:
    print("Вы не прошли тест")
elif 50 <= test <= 69:
    print("Вы не плохо прошли тест")
elif 70 <= test <= 89:
    print("Вы хорошо прошли тест")
elif 90 <= test <= 100:
    print("Вы отлично прошли тест")



    home = int(input("Введите ваш регион "))
    if home == "Япония" or "япония":
        print("こんにちは、私はあなたのアシスタントのジェイクです。")
    elif home == "Россия" or "россия":
        print("Здравствуйте, я ваш помощник Джейк.")
    elif home == "Южная Корея" or "южная Корея":
        print("안녕하세요, 저는 귀하의 보조 제이크입니다.")
    elif home == "Америка" or "америка":
        print("Hello, I'm your assistant Jake.")
    elif home == "Франция" or "франция":
        print("Bonjour, je suis votre assistant Jake.")
    else :
        print("Ваш регион не поддерживаеться.")