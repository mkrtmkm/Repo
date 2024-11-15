f = open("input13.1.txt")
for line in f:
    words = line.split()
    for word in words:
        print(len(word), end =" ")

f.close()