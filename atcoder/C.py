import heapq
n = int(input())
current = []
d = {}
numbers = [int(i) for i in input("").split(" ")]
for i in range(len(numbers)):
  number = numbers[i]
  if(number in d and d[number]):
    heapq.heappush(current,(i,number))
    d[number] = False
  elif(number not in d):
    d[number] = True
while current:
  print(heapq.heappop(current)[1],end=" ")
