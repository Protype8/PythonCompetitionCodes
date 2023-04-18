def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    inpu = input("")
    if(inpu in "codeforces"):
      print("YES")
    else:
      print("NO")
if __name__ == "__main__":
  main()