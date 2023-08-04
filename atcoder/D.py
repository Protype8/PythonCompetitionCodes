n = int(input())
meals = []
for _ in range(n):
  meals.append(input("").split(" "))
#First is not poisoned second is posined
dp =[[0,0] for i in range(n+1)]
for i in range(1,len(meals)+1):
  if(meals[i-1][0] == "1"):
    dp[i][1] = max(dp[i-1][0]+int(meals[i-1][1]),dp[i-1][1])
    dp[i][0] = dp[i-1][0]
  else:
    dp[i][0] = max(dp[i-1][1]+int(meals[i-1][1]),dp[i-1][0]+int(meals[i-1][1]),dp[i-1][0])
    dp[i][1] = dp[i-1][1]
print(max(dp[-1]))
