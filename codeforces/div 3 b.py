import string
def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    lowercases = string.ascii_lowercase
    uppercases = string.ascii_uppercase
    a,k = input("").split(" ")
    k = int(k)
    s = input("")
    res = 0
    d = {}
    for char in s:
      d[char] = d.get(char,0)+1
    for i in range(len(lowercases)):
      low_count,high_count = d.get(lowercases[i],0),d.get(uppercases[i],0)
      m = min(low_count, high_count)
      if(m != 0):
        d[lowercases[i]] -= m
        d[uppercases[i]] -= m
        res += m
    i= 0
    while i < len(lowercases):
      if(d.get(lowercases[i],0) >= 2):
        k -= 1
        res += 1
        d[lowercases[i]] -= 2
        if(k == 0):
          break
      if(d.get(uppercases[i], 0) >= 2):
        k -= 1
        res += 1
        d[uppercases[i]] -= 2
        if(k == 0):
          break
      if(d.get(lowercases[i],0) <= 1 and d.get(uppercases[i],0) <= 1):
        i+=1
    print(res)
if __name__ == "__main__":
  main()