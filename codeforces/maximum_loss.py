from itertools import combinations_with_replacement
ways = [0,-1]
def main():
  test_cases = int(input(""))
  for i in range(test_cases):
    list_a_length = int(input(""))
    list_a = [int(i) for i in input("").split(" ")]
    list_b_length = int(input(""))
    list_b = [int(i) for i in input("").split(" ")]
    total_answers = int(input(""))
    total_sum = 0
    for r in range(0,total_answers+1):
      a_sum = 0
      b_sum = 0
      if(r <= list_a_length and total_answers-r <= list_b_length):
        for a_start in range(r+1):
            a_end = r-a_start
            a_list_copy = list_a.copy()
            current_sum = 0
            for _ in range(a_start):
              current_sum += a_list_copy.pop(0)
            for _ in range(a_end):
              current_sum += a_list_copy.pop()
            if(current_sum > a_sum):
              a_sum = current_sum
        for b_start in range(total_answers-r+1):
            b_end = total_answers-r-b_start
            b_list_copy = list_b.copy()
            current_sum = 0
            for _ in range(b_start):
              current_sum += b_list_copy.pop(0)
            for _ in range(b_end):
              current_sum += b_list_copy.pop()
            if(current_sum > b_sum):
              b_sum = current_sum
        if(b_sum+a_sum > total_sum):
          total_sum = b_sum+a_sum
    print(f"Case #{i+1}: {total_sum}")
if __name__ == "__main__":
  main()