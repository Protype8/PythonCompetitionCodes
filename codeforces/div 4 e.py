def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    length = int(input(""))
    lis = [int(i) for i in input("").split(" ")]
    if (length == 2):
      if ((lis[0] > 0 and lis[1] > 0) or (lis[0] < 0 and lis[1] < 0)):
        print(abs(sum(lis)))
      else:
        print(abs(lis[1]) if abs(lis[0]) < abs(lis[1]) else abs(lis[0]))
      return
    for i in range(1,len(lis)-1):
      if(lis[i] < 0):
        if(abs(lis[i]) > abs(lis[i-1]) or lis[i-1] < 0):
          lis[i] *= -1
          lis[i-1] *= -1
        elif(abs(lis[i]) > abs(lis[i+1]) or lis[i-1] < 0):
          lis[i] *= -1
          lis[i + 1] *= -1
    print(sum(lis))
if __name__ == "__main__":
  main()