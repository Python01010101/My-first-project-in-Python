import os
os.system('cls' if os.name == 'nt' else 'clear')


home = input("Введите ваш регион: ").strip()  # убираем пробелы по краям
home = home.lower()  # делаем ввод в нижнем регистре для унификации

if home == "япония":
    print("こんにちは、私はあなたのアシスタントのジェイクです。")
elif home == "россия":
    print("Здравствуйте, я ваш помощник Джейк.")
elif home == "южная корея":
    print("안녕하세요, 저는 귀하의 보조 제이크입니다.")
elif home == "америка":
    print("Hello, I'm your assistant Jake.")
elif home == "франция":
    print("Bonjour, je suis votre assistant Jake.")
else:
    print("Ваш регион не поддерживается.")
