def operations(numbers):
    count = 0
    summa = 0
    max_el = 0
    min_el = 999999999

    try:
        while True:
            number = numbers[count]
            summa += number
            number = abs(number)

            if number > max_el:
                max_el = number
            if number < min_el and number != 0:
                min_el = number

            count += 1

    except IndexError:
        pass

    max_dif = max_el / min_el

    return count, summa, max_dif


numbers = list(map(float, input().split()))

count, summa, max_dif = operations(numbers)

print(f"Кількість елементів у списку = {count}" "\n"
    f"Сума елементів списку = {summa}" "\n"
    f"Значення найбільшого відношення = {max_dif} ")
