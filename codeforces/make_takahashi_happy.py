H,W = [int(i) for i in input().split(" ")]
grid = []
for _ in range(H):
  grid.append([int(i) for i in input().split(" ")])
visited = set()
def dfs(i,j):
  if (i not in range(H) or j not in range(W) or grid[i][j] in visited):
    return 0
  if(i == H-1 and j == W-1):
    return 1
  visited.add(grid[i][j])
  res = dfs(i+1,j)+dfs(i,j+1)
  visited.remove(grid[i][j])
  return res
print(dfs(0,0))