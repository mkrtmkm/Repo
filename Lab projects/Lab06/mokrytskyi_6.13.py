n = input()
sort = []

for i in n:
    if i != ' ':
        sort.append(i)

for i in range(len(sort)):
    for j in range(i + 1, len(sort)):
        if sort[i] > sort[j]:
            sort[i], sort[j] = sort[j], sort[i]

sort_str = ""
for с in sort:
    sort_str += с

print(sort_str)