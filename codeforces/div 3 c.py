import string
import heapq
def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    input("")
    cards = [int(i) for i in input().split(" ")]
    card_stack = []
    power = 0
    for card in cards:
      if card != 0:
        heapq.heappush(card_stack,-card)
      elif(card_stack):
        power += heapq.heappop(card_stack)
    print(abs(power))
if __name__ == "__main__":
  main()