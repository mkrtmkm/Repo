def all_lines(f):
    lines = []
    with open(f, "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line.strip())
    return "\n".join(lines)

def long_line(f, leng=60):
    long = []
    with open(f, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > leng:
                long.append(line.strip())
    return "\n".join(long)

def empty_line(f):
    count_empty = 0
    with open(f, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == " ":
                count_empty += 1
    return count_empty

def longest_line(f):
    longest = " "
    with open(f, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > len(longest):
                longest = line.strip()
    return longest

f = "input13.1.txt"
print(all_lines(f))
print("-----------")
print(long_line(f))
print("-----------")
print(empty_line(f))
print("-----------")
print(longest_line(f))


