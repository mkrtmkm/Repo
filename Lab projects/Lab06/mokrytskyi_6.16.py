s = input()

if len(s) <= 10:
    print(" ")
else:
    word1 = s[2] + s[6] + s[10]
    print(word1)

    word2 = s[0] + s[-2] + s[-1]
    print(word2)

    word3 = s[:7]
    print(word3)

    word4 = s[4:]
    print(word4)

    word5 = s[1::2]
    print(word5)

    length_word5 = len(word5)
    print(length_word5)

    revers = s[::-1]
    print(revers)