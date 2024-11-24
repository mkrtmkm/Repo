def write_text_to_file(text, filename):
    with open(filename, "w") as file:
        for i in range(0, len(text), 40):
            file.write(text[i:i+40] + "\n")


input_text = input()
write_text_to_file(input_text, "output13.6.txt")

print("Файл створено")
