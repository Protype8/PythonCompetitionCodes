H,W = [int(i) for i in input("").split(" ")]
grid = []
for _ in range(H):
  grid.append(list(input()))
a = W
c = H
b = d = -1
up_found = False
for i in range(H):
  left_found = False
  for j in range(W):
    if(grid[i][j] == "#"):
      if (up_found):
        if (i > d):
          d = i
      else:
        if (i < c):
          c = i
        up_found = True
      if(left_found):
        if(j > b):
          b = j
      else:
        if(j < a):
          a = j
        left_found = True
for i in range(c,d+1):
  for j in range(a,b+1):
    if(grid[i][j] == "."):
      print(i+1,j+1)
      break
  else:
    continue
  break