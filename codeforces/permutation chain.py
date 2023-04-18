import math
def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    n = int(input())
    print(n)
    permutation = [i for i in range(1,n+1)]
    print(*permutation)
    permutation[0],permutation[-1] = permutation[-1],permutation[0]
    print(*permutation)
    fixedness = n-2
    current_count = 1
    while fixedness > 0:
      permutation[current_count],permutation[-1] = permutation[-1],permutation[current_count]
      fixedness -= 1
      current_count += 1
      print(*permutation)
if __name__ == "__main__":
  main()