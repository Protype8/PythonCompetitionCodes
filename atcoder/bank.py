import heapq
n,q = [int(i) for i in input().split(" ")]
current = 1
cur = []
res = []
for _ in range(q):
  event = int(input())
  if(event == 1):
    heapq.heappush(cur,current)
    current += 1
  elif(event == 2):
    cur[i] = cur[-1]
    cur.pop()
    if i < len(h):
      heapq._siftup(h, i)
      heapq._siftdown(h, 0, i)
  else:
    res.append(heapq.heappop())