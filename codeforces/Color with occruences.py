def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    string = input("")
    no_of_sub = int(input(""))
    colored = [False for _ in string]
    subs = {}
    for i in range(no_of_sub):
      sub = input("")
      subs[sub] = i+1
    sorted_subs = list(subs.keys())
    sorted_subs.sort()
    sorted_subs.sort(key=len,reverse=True)
    counts = 0
    patterns = []
    for sub in sorted_subs:
      index = 0
      while 1:
        index = string.find(sub,index)
        if(index == -1):
          break
        valid = False
        for i in range(index, index + len(sub)):
          if(colored[i] == False):
            valid = True
            break
        if(valid):
          counts+=1
          patterns.append([subs[sub],index+1])
          for i in range(index,index+len(sub)):
            colored[i] = True
        index +=1
    if(counts > 0):
      print(counts)
      for pattern in patterns:
        print(pattern[0],pattern[1])
    else:
      print(-1)
if __name__ == "__main__":
  main()