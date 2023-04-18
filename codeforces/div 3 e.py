import string
def dfs(s,t,i,k):
  if(i == len(s)):
    if("".join(s) == t):
      return True
    else:
      return False
  if(s[i] == t[i]):
    return dfs(s,t,i+1,k)
  else:
    if (i + 1 < len(s) and s[i + 1] == t[i]):
      s[i + 1], s[i] = s[i], s[i + 1]
      if(dfs(s,t,i+1,k)):
        return True
      s[i + 1], s[i] = s[i], s[i + 1]
    if (i + k < len(s) and s[i + k] == t[i]):
      s[i + k], s[i] = s[i], s[i + k]
      if(dfs(s,t,i+1,k)):
        return True
      s[i + k], s[i] = s[i], s[i + k]
    if (i + k + 1 < len(s) and s[i + k + 1] == t[i]):
      s[i + k + 1], s[i] = s[i], s[i + k + 1]
      if(dfs(s, t, i + 1,k)):
        return True
      s[i + k + 1], s[i] = s[i], s[i + k + 1]
  return False
def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    l,k = input().split(" ")
    k = int(k)
    s,t = list(input()),input()
    if(dfs(s,t,0,k)):
      print("YES")
    else:
      print("NO")
if __name__ == "__main__":
  main()