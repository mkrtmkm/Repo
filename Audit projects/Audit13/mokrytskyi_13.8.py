def read_polinom(filename):
    coefs = {}
    with ("polinom.txt") as f:
        for line in f:
            power, coef = line.split()
            coef = float(coef)
            coefs[power] = coef
    return coefs


def derivative(coefs):
    derivative_poly = {}
    for power, coef in coefs.items():
        if power > 0:
            derivative_poly[power - 1] = power * coef
    return derivative_poly


