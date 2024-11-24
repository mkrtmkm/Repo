from math import sqrt

def even(numbers):
    return sum(1 for num in numbers if num % 2 == 0)

def squares(numbers):
    return sum(1 for num in numbers if sqrt(num).is_integer() and int(sqrt(num)) % 2 != 0)

def difference(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    if evens and odds:
        return max(evens) - min(odds)
    return None

def length(numbers):
    if not numbers:
        return 0

    longest = 0
    current_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_length += 1
        else:
            longest = max(longest, current_length)
            current_length = 1

    return max(longest, current_length)

with open("import13.5.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

a = even(numbers)
b = squares(numbers)
c = difference(numbers)
d = length(numbers)

print(f"Кількість парних чисел: {a}")
print(f"Кількість квадратів непарних чисел: {b}")
print(f"Різниця між найбільшим парним і найменшим непарним: {c}")
print(f"Кількість компонент у найдовшій зростаючій послідовності: {d}")


