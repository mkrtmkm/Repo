def mult(n, m):
   if m == 0:
       return 0
   return mult(n, m-1) + n

n = int(input())
m = int(input())

print(mult(n, m))