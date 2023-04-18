import math
def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    n = int(input())
    moves = math.inf
    check_nums = {1:2,2:1,3:1,4:2}
    for num in check_nums:
      if((n-num)%3==0 and n-num >= 0):
        current_moves = (n-num)//3+check_nums[num]
        if(current_moves < moves):
          moves = current_moves
    print(moves)
if __name__ == "__main__":
  main()