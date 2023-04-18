import string
import heapq
def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    input()
    s = input()
    seen = set()
    for i in range(0,len(s)-1):
      if(s[:i]+s[i+2:] not in seen):
        seen.add(s[:i]+s[i+2:])
    print(len(seen))
if __name__ == "__main__":
  main()