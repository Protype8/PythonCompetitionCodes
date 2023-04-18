import string
import time
def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    tiles = [string.ascii_lowercase.index(i)+1 for i in input("")]
    #cost of a - e is same as cost of a - c - e so cost of l-c is same as l-i-g-c in logic
    dir = 1 if tiles[0] < tiles[-1] else -1
    ans = []
    sequence = []
    for i in range(tiles[0],tiles[-1]+dir,dir):
      if(i in tiles):
        for a in range(len(tiles)):
          if(tiles[a] == i):
            ans.append(i)
            sequence.append(a+1)
    cost = 0
    for i in range(1,len(ans)):
      cost += abs(ans[i]-ans[i-1])
    print(cost,len(ans))
    print(*sequence)

if __name__ == "__main__":
  main()