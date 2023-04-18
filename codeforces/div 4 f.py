def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    length,queries = input("").split(" ")
    lis = [int(i) for i in input("").split(" ")]
    queries = int(queries)
    for i in range(queries):
      query = [int(i) for i in input("").split(" ")]
      if(len(query) == 3):
        for i in range(query[1]-1,query[2]):
          a = lis[i]
          s = 0
          while a > 0:
            s += a % 10
            a = a // 10
          lis[i] = s
      elif(len(query) == 2):
        print(lis[query[1]-1])
if __name__ == "__main__":
  main()