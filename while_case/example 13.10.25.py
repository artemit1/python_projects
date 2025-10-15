c
num_of_day = int(input("Введи номер дня тижня: "))
if num_of_day == 1:
    print("Понеділок")

match num_of_day:
    case 1:
        print("Понеділок")
    case 2:
        print("Вівторок")
    case 3:
        print("Середа")
    case 4:
        print("Четвер")
    case 5:
        print("Пятниця")
    case 6:
        print("Субота")
    case 7:
        print("Неділя")

    case _:
        print("Такого дня немає")



num_of_month = int(input("Введи номер місяця: "))
match num_of_month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12 :
        print("31 день у місяці")

    case 4 | 6 | 9 | 11:
        print("30 днів у місяці")

    case 2:
        print("28 або 29 днів")

    case _:
        print("Такого місяця не існує")





cost = 10000
cost_1 = int(input("Введи вартість товару: "))
discount = 0
if cost_1 >= 5000 and cost_1 <= 10000:
    discount = 10
    cost_1 = cost_1 - (cost_1  *  discount / 100)
    print(f"Вартість після знижки {cost_1:.2f}")

elif cost_1 > 10000 and cost_1 <= 2000:
    discount = 20
    cost_1 = cost_1 - (cost_1  *  discount / 100)
    print(f"Вартість після знижки {cost_1:.2f}")

elif cost_1 > 20000 :
    discount = 30
    cost_1 = cost_1 - (cost_1  *  discount / 100)
    print(f"Вартість після знижки {cost_1:.2f}")

elif cost_1 > 0:
    discount = 0
    cost_1 = cost_1 - (cost_1  *  discount / 100)
    print(f"Вартість після знижки {cost_1:.2f}")

else:
    print("Вартість не може бути відємна")







