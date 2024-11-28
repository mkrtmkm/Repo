import os

def read_polinom(filename):
    coefs = {}
    try:
        if not os.path.isfile(filename):
            raise FileNotFoundError (f"Файл '{filename}' не знайдено")

        with open(filename, "r") as f:
            for line in f:
                try:
                    power, coef = map(float, line.split())
                    if power < 0 or not power.is_integer():
                        raise KeyError(f"Степінь {power} не є невід'ємним цілим числом")
                    coefs[int(power)] = coef
                except ValueError:
                    print(f"Неправильний формат даних у файлі '{filename}': '{line.strip()}'")

    except FileNotFoundError as e:
        print(f"Помилка доступу до файлу: {e}")
        exit()
    except KeyError as e:
        print(f"Помилка у файлі '{filename}': {e}")
        exit()
    return coefs

def derivative(coefs):
    derivative_poly = {}
    for power, coef in coefs.items():
        if power > 0:
            derivative_poly[power - 1] = power * coef
    return derivative_poly

def add_poly(poly1, poly2):
    res = poly1.copy()
    for power, coef in poly2.items():
        res[power] = res.get(power, 0) + coef
    return res

def multiply_poly(poly1, poly2):
    res = {}
    for power1, coef1 in poly1.items():
        for power2, coef2 in poly2.items():
            power = power1 + power2
            coef = coef1 * coef2
            res[power] = res.get(power, 0) + coef
    return res

def canonical_form(polynomial):
    terms = []
    for power in sorted(polynomial.keys(), reverse=True):
        coef = polynomial[power]
        if coef == 0:
            continue
        if power == 0:
            terms.append(f"{coef}")
        elif power == 1:
            terms.append(f"{coef}x")
        else:
            terms.append(f"{coef}x^{power}")
    return "+".join(terms).replace("+-", "-")
def write_polynom(filename, content):
    if os.path.isfile(filename):
        ask1 = input(f"Файл '{filename}' вже існує. Замінити його? (так/ні): ").strip().lower()
        if ask1 == "так":
            with open(filename, "w", encoding='utf-8') as file:
                file.write(content)
            print(f"Результат успішно записано у файл '{filename}'.")
        if ask1 == "ні":
            filename2 = input("Введіть назву нового файлу з розширенням '.txt' ")
            with open(filename2, "w", encoding='utf-8') as file:
                file.write(content)
            print(f"Результат успішно записано у файл '{filename2}'.")

P = read_polinom("poly1.13.8.txt")
R = read_polinom("poly2.13.8.txt")

P_derivative = derivative(P)
P_plus_R = add_poly(P, R)
P_times_R = multiply_poly(P, R)

output_content = (
    "Похідна P(x):\n" + canonical_form(P_derivative) + "\n\n" +
    "Сума P(x) та R(x):\n" + canonical_form(P_plus_R) + "\n\n" +
    "Добуток P(x) та R(x):\n" + canonical_form(P_times_R) + "\n"
)

write_polynom("output13.8.txt", output_content)