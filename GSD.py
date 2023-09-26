def find_gcd(first, second):
    # Вибираємо менше з двох чисел та привласнюємо його значення змінній gcd
    if first < second:
        gcd = first
    else:
        gcd = second
    
    # Поки gcd не є НСД для обох чисел, зменшуємо його на одиницю
    while True:
        if first % gcd == 0 and second % gcd == 0:
            break
        gcd -= 1
    
    return gcd

# Зчитуємо два додатні цілі числа від користувача
first = int(input("Введіть перше число: "))
second = int(input("Введіть друге число: "))

# Знаходимо та виводимо НСД
result = find_gcd(first, second)
print("НСД чисел", first, "і", second, "дорівнює", result)
