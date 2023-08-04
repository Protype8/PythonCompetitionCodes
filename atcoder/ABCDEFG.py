import string
d = {"A":3,"B":1,"C":4,"D":1,"E":5,"F":9}
p,q = sorted(input("").split(" "))
current = string.ascii_uppercase.index(p)
res = 0
while string.ascii_uppercase[current] != q:
  res += d[string.ascii_uppercase[current]]
  current+=1
print(res)