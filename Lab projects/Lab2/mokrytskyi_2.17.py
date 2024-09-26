cx, cy = [int(d) for (d) in input().split()]
ax, ay = [int(d) for (d) in input().split()]
bx, by = [int(d) for (d) in input().split()]

condition1 = (bx - ax)*(cy - ay) == (by - ay)*(cx - ax)
condition2 = (cx - ax)*(bx - ax) >= 0 and  (cy - ay)*(by - ay) >= 0
condition3 =  min(ax, bx) <= cx <= max(ax, bx) and min(ay, by) <= cy <= max(ay, by)
if  condition1:
   print("YES")
else:
    print("NO")

if condition1 and condition2:
    print("YES")
else:
    print("NO")

if condition1 and condition3:
    print("YES")
else:
    print("NO")