def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    _ = input("")
    lis = [int(i) for i in input("").split(" ")]
    list_len = len(lis)
    already = set()
    count = 0
    out = 0
    for i in range(list_len-1,-1,-1):
      already.add(lis[i])
      count+=1
      if(len(already) != count):
        out = list_len-(count-1)
        break
    print(out)
if __name__ == "__main__":
  main()