import math
def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    a,b,c = [int(i) for i in input().split(" ")]
    distance_a = abs(a-1)
    distance_b = abs(c-b)+abs(c-1)
    if(distance_a < distance_b):
      print(1)
    elif(distance_a > distance_b):
      print(2)
    else:
      print(3)

if __name__ == "__main__":
  main()