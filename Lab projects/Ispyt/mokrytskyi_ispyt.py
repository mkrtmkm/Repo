from math import sqrt
import os
def discriminant(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        root1 = (-b + sqrt(D)) / (2*a)
        root2 = (-b - sqrt(D)) / (2 * a)
        return a, b, c, root1, root2

    elif D==0:
        root = -b / (2*a)
        return a, b, c, root

    else:
        return a, b, c, None

filename = "input_2.txt"
output_file = "output.txt"
try:
    if not os.path.isfile(filename):
        raise FileNotFoundError

    no_roots = []
    one_root = []
    two_roots = []

    with open(filename, "r") as file:
        for line in file:
            try:
                a, b, c = map(float, line.split())
                res = discriminant(a, b, c)

                if len(res) == 5:
                    two_roots.append(res)
                elif res[-1] is None:
                    no_roots.append(res)
                else:
                    one_root.append(res)
            except ValueError:
                print(f"Увага: Некоректні дані у рядку: '{line.strip()}'")

except FileNotFoundError as e:
    print(e)
    with open(output_file, "w") as out_file:

        for eq in two_roots:
            out_file.write(f"{eq[0]} {eq[1]} {eq[2]} {eq[3]} {eq[4]}\n")
        for eq in one_root:
            out_file.write(f"{eq[0]} {eq[1]} {eq[2]} {eq[3]}\n")
        for eq in no_roots:
            out_file.write(f"{eq[0]} {eq[1]} {eq[2]} None\n")

print(f"Файл '{output_file}' створено успішно.")



