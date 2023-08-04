l = [int(i) for i in input("").split(" ")]
res = 0
for i in range(len(l)):
  res += l[i]*pow(2,i)
print(res)