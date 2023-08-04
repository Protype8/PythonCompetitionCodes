N = int(input())
walks = [int(i) for i in input("").split(" ")]
cur_sum = 0
res = []
for i in range(len(walks)):
  if(i%7 == 0 and i != 0):
    res.append(cur_sum)
    cur_sum = 0
  cur_sum += walks[i]
res.append(cur_sum)
for r in res:
  print(r,end=" ")