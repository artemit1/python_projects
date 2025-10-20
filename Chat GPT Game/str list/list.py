list_of_student = ["a","b","c","d","e","f","g","h","i","j"]
list_of_numbers = [1,2,3,4,5,6,7,8,9]
list_of_bool = [True,False,True,False]



print(list_of_student[::2])


list_blank = []

list_blank.append("Chernivtsi")
print(list_blank)

list_blank.append("Kiev")
print(list_blank)

list_blank.insert(1,"Lvov")
print(list_blank)

# добавити декілька
list_blank.extend(["IF","Sumy"])
print(list_blank)

# розмір , довжина
print(len(list_blank))

# видалення
# останній
list_blank.pop(0)
print(list_blank)

# видалення по значення
list_blank.remove("Kiev")
print(list_blank)

#все очитстити
list_blank.clear()
print(list_blank)



list_num = [3,413,2,8923,241,43,234,11,9]
print(f"Кількість чисел: {len(list_num)}")
print(f"Сума чисел: {sum(list_num)}")
print(f"Макс число: {max(list_num)}")
print(f"Мін число: {min(list_num)}\n")

# сортування
list_num.sort()
print(f"Сортування: {list_num}")

# обернено
list_num.reverse()
print(f"Обернуто: {list_num}\n")


print(f"Кількість цифри 7: {list_num.count(7)}")
print(f"Кількість цифри 7: {list_num.count(7)}")