# 1
def show_quote():
    print("Don't compare yourself with anyone in this world…")
    print("    if you do so, you are insulting yourself.")
    print("        Bill Gates")


show_quote()
# 2
def show_even_numbers(start, end):
    print(f"Парні числа між {start} і {end}:")
    for number in range(start + 1, end):
        if number % 2 == 0:
            print(number)


show_even_numbers(3, 15)

# 4
def find_min(a, b, c, d, e):
    return min(a, b, c, d, e)

# Приклад виклику
result = find_min(12, 5, 9, 3, 15)
print("Мінімальне число:", result)

