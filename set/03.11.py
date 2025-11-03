# 1
def calculate_discount(price, precent):
    discount = price * (precent / 100)
    final_price = price - discount
    return final_price




a = calculate_discount(20, 80)
print(a)

# 2
def to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

b = to_fahrenheit(20)
print(b)

# 3
def get_grade(points):
    if points >= 90:
        return "Відмінно"
    elif points >= 70:
        return "Добре"
    elif points >= 50:
        return "Задовільно"
    else:
        return "Незадовільно"

print(get_grade(91))

# 4
def rectangle_area(width, height):
    area = width * height
    return area

ab = rectangle_area(100, 100)
print(ab)

# 5
def analyze_number(num):
    if num > 0:
        return "Додатнє"
    elif num < 0:
        return "Відємне"
    elif num == 0:
        return ("Нуль")

number = analyze_number(100)
print(number)

# 6
def average_of_three(a, b, c):
    zxc = a + b + c
    pp = zxc / 3
    return pp

asd = average_of_three(5, 4, 3)
print(asd)

# 7
def word_lenght(word):
    return len(word)

zz = word_lenght("hello")
print(zz)

# 8
def convert_to_usd(amount_uah, rate):
    aaa = amount_uah * rate
    return aaa

hu = convert_to_usd(50, 0.024)
print(hu)

# 9
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

tung = is_even(10)
print(tung)