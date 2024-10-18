M = int(input())
if M >= 100:
    if M // 100 == 1:
        print("one hundred", end=" ")
    elif M // 100 == 2:
        print("two hundred", end=" ")
    elif M // 100 == 3:
        print("three hundred", end=" ")
    elif M // 100 == 4:
        print("four hundred", end=" ")
    elif M // 100 == 5:
        print("five hundred", end=" ")
    elif M // 100 == 6:
        print("six hundred", end=" ")
    elif M // 100 == 7:
        print("seven hundred", end=" ")
    elif M // 100 == 8:
        print("eight hundred", end=" ")
    elif M // 100 == 9:
        print("nine hundred", end=" ")

    M %= 100

if 10 < M < 20:
    if M == 11:
        print("eleven", end="")
    elif M == 12:
        print("twelve", end="")
    elif M == 13:
        print("thirteen", end="")
    elif M == 14:
        print("fourteen", end="")
    elif M == 15:
        print("fifteen", end="")
    elif M == 16:
        print("sixteen", end="")
    elif M == 17:
        print("seventeen", end="")
    elif M == 18:
        print("eighteen", end="")
    elif M == 19:
        print("nineteen", end="")

else:
    if M >= 10:
        if M // 10 == 1:
            print("ten", end=" ")
        elif M // 10 == 2:
            print("twenty", end=" ")
        elif M // 10 == 3:
            print("thirty", end=" ")
        elif M // 10 == 4:
            print("forty", end=" ")
        elif M // 10 == 5:
            print("fifty", end=" ")
        elif M // 10 == 6:
            print("sixty", end=" ")
        elif M // 10 == 7:
            print("seventy", end=" ")
        elif M // 10 == 8:
            print("eighty", end=" ")
        elif M // 10 == 9:
            print("ninety", end=" ")

    M %= 10

    if M == 1:
        print("one", end="")
    elif M == 2:
        print("two", end="")
    elif M == 3:
        print("three", end="")
    elif M == 4:
        print("four", end="")
    elif M == 5:
        print("five", end="")
    elif M == 6:
        print("six", end="")
    elif M == 7:
        print("seven", end="")
    elif M == 8:
        print("eight", end="")
    elif M == 9:
        print("nine", end="")

print()