# 1
balance = 5000
print(f"Ваш поточний баланс - {balance} грн")
while True:
    a = str(input("Оберіть дію для взаємодії з балансом(зняти, поповнити, вийти) - "))

    if a == "вийти":
        print(f"Ваш кінцевий баланс - {balance} грн, гарного дня!")
        break

    elif a == "зняти":
        b = int(input("Введіть суму для зняття: "))
        if b > balance:
            print("Недостатньо коштів, спробуйте ще раз")
        elif b < balance:
            c = balance - b
            print(f"Ви зняли {b} грн, ваш баланс - {c} грн")


    elif a == ("поповнити"):
        d = int(input("Введіть суму для поповнення балансу - "))
        if d < 0:
            print("Сума не може бути меньше за 0")
        else:
            e = balance + d
            print(f"Ваш баланс попвнено на {d} грн, ваш баланс - {e} грн")


# 2
print("Вітаємо на екзамені! Введіть 'стоп', щоб завершити достроково.\n")

score = 0
question_num = 0


while question_num < 5:
    question_num += 1
    print(f"Питання {question_num}:")

    # приклад запитань (можна замінити на будь-які)
    if question_num == 1:
        answer = input("Скільки буде 5 + 7? ").strip().lower()
        if answer == "12":
            print("Правильно!")
            score += 1
        elif answer == "стоп":
            break
        else:
            print("Неправильно!")

    elif question_num == 2:
        answer = input("Яка столиця України? ").strip().lower()
        if answer == "київ":
            print("Правильно!")
            score += 1
        elif answer == "стоп":
            break
        else:
            print("❌ Неправильно!")

    elif question_num == 3:
        answer = input("Скільки днів у тижні? ").strip().lower()
        if answer == "7" or answer == "сім":
            print("Правильно!")
            score += 1
        elif answer == "стоп":
            break
        else:
            print("❌ Неправильно!")

    elif question_num == 4:
        answer = input("Який колір отримуємо, змішавши жовтий і синій? ").strip().lower()
        if answer == "зелений":
            print("Правильно!")
            score += 1
        elif answer == "стоп":
            break
        else:
            print("Неправильно!")

    elif question_num == 5:
        answer = input("Яка найбільша планета Сонячної системи? ").strip().lower()
        if answer == "юпітер":
            print("Правильно!")
            score += 1
        elif answer == "стоп":
            break
        else:
            print("Неправильно!")

    print()  # порожній рядок між питаннями

# кінець тесту
print("Екзамен завершено!")
print(f"Ваш результат: {score} з {question_num} можливих балів.")

# оцінка
if score == 5:
    print("Оцінка: 12 — Відмінно!")
elif score >= 3:
    print("Оцінка: 8 — Добре!")
elif score >= 1:
    print("Оцінка: 5 — Задовільно.")
else:
    print("Оцінка: 2 — Потрібно підтягнути знання.")





# 3
juice = 1000  # початковий об’єм соку в мл
print("У пляшці 1000 мл соку.")

while juice > 0:
    try:
        a = int(input("Скільки мл соку ви випили? "))
    except ValueError:
        print("Будь ласка, введіть число!")
        continue  # повертаємось на початок циклу

    if a <= 0:
        print("Сума має бути більшою за 0.")
        continue

    if a > juice:
        print("Ви не можете випити більше, ніж залишилось!")
        continue

    juice -= a  # зменшуємо залишок

    if juice > 0:
        print(f"Залишилось {juice} мл соку.")
    else:
        print("Сік закінчився! 🧃")







