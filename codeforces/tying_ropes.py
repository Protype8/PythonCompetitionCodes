N,T = [int(i) for i in input().split(" ")]
graph_dict = {i:[] for i in range(1,N+1)}
for _ in range(T):
  a,b,c,d = input().split(" ")
  graph_dict[int(a)].append(int(c))
groups = 0
circles = 0