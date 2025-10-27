student = {"name": "Nazar", "age": 22, "position": "teacher"}

person = {"name": "Anna", "city": "Kyiv"}
print(person)

# додавання елемента у словник
person["age"] = 20
print(person)

# змінити елемент
person["city"] = "Lviv"

# del - видалення по ключу
if "phoneNumber" in person:
    del person["phoneNumber"]
print(person)

# pop - видалити і дальше зберігати у змінній
removed_value = person.pop("city", "Ключ не знайдено")
print(removed_value)

print(person)

# діставання елемента по ключі
print(person["name"])

# дістати всі ключі
print(person.keys())

# дістати всі значення
print(person.values())

# дістати всі елементи з ключами
print(person.items())

# оновити
person.update({"city": "Sumy"})
print(person)

# перевірка чи є ключ в словнику


if "name" in person:
    print('Імя є у списку')



