def create_file():
    with open("output13.3.txt", "w") as file:
        for i in range(1, 10):
            file.write(str(i)*i + "\n")

create_file()