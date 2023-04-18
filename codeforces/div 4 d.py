def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    length = int(input(""))
    string = input("")
    right_count = {i:string.count(i) for i in set(string)}
    left_count = {}
    m = len(left_count)+len(right_count)
    for i in range(0,length):
      right_count[string[i]] -= 1
      if(right_count[string[i]] == 0):
        del right_count[string[i]]
      left_count[string[i]] = left_count.get(string[i],0)+1
      m = max(len(left_count)+len(right_count),m)
    print(m)
if __name__ == "__main__":
  main()