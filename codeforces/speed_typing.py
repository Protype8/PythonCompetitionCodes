
def check_subsequnce(P,T):
  p_length = len(P)
  t_length = len(T)
  p_pointer = 0
  t_pointer = 0
  if(p_length < t_length):
      return "IMPOSSIBLE"
  while p_pointer < p_length and t_pointer < t_length:
    if (T[t_pointer] == P[p_pointer]):
      p_pointer = p_pointer + 1
      t_pointer = t_pointer + 1
    else:
      p_pointer = p_pointer + 1
  if t_pointer == t_length:
    return p_length-t_length
  else:
    return "IMPOSSIBLE"
def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
  # Get the grid dimensions
    T = input()
    P = input()
    answer = check_subsequnce(P,T)
    print(f'Case #{t+1}:',answer)
if __name__ == '__main__':
  main()
