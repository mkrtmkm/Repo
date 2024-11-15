def read_numbers(file_path):
    numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            numbers.extend(map(float, line.split()))
    return numbers

def summ(f):
    num = read_numbers(f)
    return sum(num)

def negative_summ(f):
    num = read_numbers(f)
    return sum(x for x in num if x < 0)

def last(f):
    num = read_numbers(f)
    return num[-1]

def maxx(f):
    num = read_numbers(f)
    return max(num)

f = "input13.2.txt"
print(f"Сума чисел = {summ(f)}")
print(f"Сума від'ємних чисел = {negative_summ(f)}")
print(f"Остання цифра = {last(f)}")
print(f"Максимальне число ={maxx(f)}")