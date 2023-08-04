import collections
import numpy
N,M,K = [int(i) for i in input().split(" ")]
g = [[0 for _ in range(N)] for _ in range(N)]
mat = {1:g}
for _ in range(M):
  a,b = [int(i) for i in input().split(" ")]
  a-=1
  b-=1
  g[a][b] = 1
  g[b][a] = 1
current_max = 1
guarded_set = set()
for _ in range(K):
  p,h = [int(i) for i in input().split(" ")]
  p-=1
  que = collections.deque()
  que.append((p,h))
  while len(que):
    p,h = que.pop()
    guarded_set.add(p+1)
    for j in range(1,h+1):
      if(not j in mat):
        mat[j] = numpy.matmul(mat[j-1],mat[1])
      for i in range(N):
        if(mat[j][p][i]):
          guarded_set.add(i+1)
print(len(guarded_set))
for i in sorted(guarded_set):
  print(i,end=" ")