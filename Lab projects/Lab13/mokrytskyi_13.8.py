def read_polinom(filename):
    coefs = {}
    with open(filename, "r") as f:
        for line in f:
            power, coef = map(float, line.split())
            coefs[int(power)] = coef
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

P = read_polinom("poly1.13.8.txt")
R = read_polinom("poly2.13.8.txt")

P_derivative = derivative(P)
P_plus_R = add_poly(P, R)
P_times_R = multiply_poly(P, R)

with open("output13.8.txt", "w", encoding='utf-8') as file:
    file.write("Похідна P(x):\n")
    file.write(canonical_form(P_derivative) + "\n\n")
    file.write("Сума P(x) та R(x):\n")
    file.write(canonical_form(P_plus_R) + "\n\n")
    file.write("Добуток P(x) та R(x):\n")
    file.write(canonical_form(P_times_R) + "\n")