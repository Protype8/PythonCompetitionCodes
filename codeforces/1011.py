def get_possible(first,second):
  s = 0
  wanted_result = second[0]
  pattern = second[1:]
  if(pattern == first[len(first)-len(pattern):]):
    change_space = first[:len(first)-len(pattern)]
    while len(change_space) > 1:
      if(wanted_result == "1"):
        f1 = int(change_space[s])
        f2 = int(change_space[s + 1])
        new_f = str(max(f1, f2))
        change_space = change_space[:s] + new_f + change_space[s + 2:]
      elif(wanted_result == "0"):
        f1 = int(change_space[s])
        f2 = int(change_space[s + 1])
        new_f = str(min(f2, f1))
        change_space = change_space[:s] + new_f + change_space[s+2:]
    if(change_space == wanted_result):
      return "Yes"
  return "No"
def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    _ = input()
    first = input()
    second = input()
    print(get_possible(first,second))
if __name__ == "__main__":
  main()
