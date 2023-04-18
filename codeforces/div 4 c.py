def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    length = input("")
    binary = input("")
    while(len(binary) > 1 and binary[0] != binary[-1]):
      binary = binary[1:-1]
    print(len(binary))
if __name__ == "__main__":
  main()