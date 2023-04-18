import heapq
def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    n = int(input(""))-1
    lis = [int(i) for i in input("").split(" ")]
    min_heap = lis.copy()
    max_heap = [-i for i in min_heap]
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    l = 0
    while l < n:
      if(min_heap[0] == lis[l] or -max_heap[0] == lis[l]):
        heapq.heappop(min_heap if min_heap[0] == lis[l] else max_heap)
        l += 1
      elif(min_heap[0] == lis[n] or -max_heap[0] == lis[n]):
        heapq.heappop(min_heap if min_heap[0] == lis[n] else max_heap)
        n -= 1
      else:
        print(l+1,n+1)
        break
    else:
      print(-1)
if __name__ == "__main__":
  main()