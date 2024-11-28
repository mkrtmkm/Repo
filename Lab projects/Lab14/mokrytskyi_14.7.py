def func():
    runtime_error_count = 0
    type_error_count = 0
    value_error_count = 0

    while True:

        user_input = input()
        if user_input.lower() == "досить":
            break

        try:
            number = float(user_input)

            if number > 9:
                raise RuntimeError
            elif number < 0:
                raise TypeError
            elif number != int(number):
                raise ValueError

        except RuntimeError:
            runtime_error_count += 1
            print("Виникла помилка RuntimeError")

        except TypeError:
            type_error_count += 1
            print("Виникла помилка TypeError")

        except ValueError:
            value_error_count += 1
            print("Виникла помилка ValueError")


    print("Підрахунок кількості виникань виключень:" "\n"
          f"RuntimeError = {runtime_error_count}" "\n"
          f"TypeError = {type_error_count}" "\n"
          f"ValueError = {value_error_count}")

func()