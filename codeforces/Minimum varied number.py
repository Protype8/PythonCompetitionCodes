def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    inp = int(input(""))
    digits = [i for i in range(9,0,-1)]
    result = ""
    for digit in digits:
      if(inp >= digit):
        inp -= digit
        result += str(digit)
    print(result[::-1])
if __name__ == "__main__":
  main()