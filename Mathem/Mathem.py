while True:
    print()
#    user_input = input("Выберите 1) sin(alpha), 2) cos(alpha), 3) tg(alpha), 4) ctg(alpha) или 'exit' для выхода: ").strip()
#    
#    if user_input.lower() == 'exit':
#        print("Выход из программы.")
#        break
#    
#    if not user_input.isdigit() or not (1 <= int(user_input) <= 4):
#        print("Введите корректное число от 1 до 4 или 'exit' для выхода.")
#        continue

    x = int(input("Выберите 1) sin(alpha), 1) cos(alpha), 3) tg(alpha), 4) ctg(alpha): "))
    f = str(input("Напишите градус и или радиан (+ или -) alpha: "))
    d = list(f.split())
    f = " ".join([d[0], d[1]])
    if x == 1 and f == "0 -":
        print("Жауабы: -sin(alpha)")
    elif x == 1 and f == "0 +":
        print("Жауабы: sin(alpha)")
    elif x == 1 and f == "90 -" or f == "pi/2 -":
        print("Жауабы: cos(alpha)")
    elif x == 1 and f == "90 +" or f == "pi/2 +":
        print("Жауабы: cos(alpha)")
    elif x == 1 and f == "180 -" or f == "pi -":
        print("Жауабы: sin(alpha)")
    elif x == 1 and f == "180 +" or f == "pi +":
        print("Жауабы: -sin(alpha)")
    elif x == 1 and f == "270 -" or f == "3pi/2 -":
        print("Жауабы: -cos(alpha)")
    elif x == 1 and f == "270 +" or f == "3pi/2 +":
        print("Жауабы: -cos(alpha)")
    elif x == 1 and f == "360 -" or f == "2pi -":
        print("Жауабы: -sin(alpha)")
    elif x == 1 and f == "360 +" or f == "2pi +":
        print("Жауабы: sin(alpha)")

    #cos
    elif x == 2 and f == "0 -":
        print("Жауабы: cos(alpha)")
    elif x == 2 and f == "0 +":
        print("Жауабы: cos(alpha)")
    elif x == 2 and f == "90 -" or f == "pi/2 -":
        print("Жауабы: sin(alpha)")
    elif x == 2 and f == "90 +" or f == "pi/2 +":
        print("Жауабы: -sin(alpha)")
    elif x == 2 and f == "180 -" or f == "pi -":
        print("Жауабы: -cos(alpha)")
    elif x == 2 and f == "180 +" or f == "pi +":
        print("Жауабы: -cos(alpha)")
    elif x == 2 and f == "270 -" or f == "3pi/2 -":
        print("Жауабы: -sin(alpha)")
    elif x == 2 and f == "270 +" or f == "3pi/2 +":
        print("Жауабы: sin(alpha)")
    elif x == 2 and f == "360 -" or f == "2pi -":
        print("Жауабы: cos(alpha)")
    elif x == 2 and f == "360 +" or f == "2pi +":
        print("Жауабы: cos(alpha)")

    #tg
    elif x == 3 and f == "0 -":
        print("Жауабы: -tg(alpha)")
    elif x == 3 and f == "0 +":
        print("Жауабы: tg(alpha)")
    elif x == 3 and f == "90 -" or f == "pi/2 -":
        print("Жауабы: ctg(alpha)")
    elif x == 3 and f == "90 +" or f == "pi/2 +":
        print("Жауабы: -ctg(alpha)")
    elif x == 3 and f == "180 -" or f == "pi -":
        print("Жауабы: -tg(alpha)")
    elif x == 3 and f == "180 +" or f == "pi +":
        print("Жауабы: tg(alpha)")
    elif x == 3 and f == "270 -" or f == "3pi/2 -":
        print("Жауабы: ctg(alpha)")
    elif x == 3 and f == "270 +" or f == "3pi/2 +":
        print("Жауабы: -ctg(alpha)")
    elif x == 3 and f == "360 -" or f == "2pi -":
        print("Жауабы: -tg(alpha)")
    elif x == 3 and f == "360 +" or f == "2pi +":
        print("Жауабы: tg(alpha)")

    #ctg
    elif x == 4 and f == "0 -":
        print("Жауабы: -ctg(alpha)")
    elif x == 4 and f == "0 +":
        print("Жауабы: ctg(alpha)")
    elif x == 4 and f == "90 -" or f == "pi/2 -":
        print("Жауабы: tg(alpha)")
    elif x == 4 and f == "90 +" or f == "pi/2 +":
        print("Жауабы: -tg(alpha)")
    elif x == 4 and f == "180 -" or f == "pi -":
        print("Жауабы: -ctg(alpha)")
    elif x == 4 and f == "180 +" or f == "pi +":
        print("Жауабы: ctg(alpha)")
    elif x == 4 and f == "270 -" or f == "3pi/2 -":
        print("Жауабы: tg(alpha)")
    elif x == 4 and f == "270 +" or f == "3pi/2 +":
        print("Жауабы: -tg(alpha)")
    elif x == 4 and f == "360 -" or f == "2pi -":
        print("Жауабы: -ctg(alpha)")
    elif x == 4 and f == "360 +" or f == "2pi +":
        print("Жауабы: ctg(alpha)")
    else:
        print("Неправильный синтаксис")

#    cont = input("Хотите продолжить? (да/нет): ").strip().lower()
#    if cont != "да":
#        print("Программа завершена.")
#        break