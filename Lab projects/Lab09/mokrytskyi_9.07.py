n = int(input())
cubes = input().strip()
missing_cubes = set()

for cube in cubes:
    if cube in missing_cubes:
        missing_cubes.remove(cube)
    else:
        missing_cubes.add(cube)

if missing_cubes:
    print(missing_cubes.pop())
else:
    print("Ok")