color_dict = {"O":["R","Y"],"P":["R","B"],"G":["Y","B"],"A":["R","Y","B"]}
primary_colors = ["R","B","Y"]
# function to return key for any value
def get_key(val):
  for key, value in color_dict.items():
       if val == value:
           return key
  return None
def get_number_of_strokes(string):
  string = list(string)
  strokes = 0
  for primary_color in primary_colors:
    last_pos = -10000
    min_strokes = 0
    for i in range(len(string)):
      if (string[i] == primary_color):
        if(last_pos != i-1):
          min_strokes+=1
        last_pos = i
      elif(string[i] in color_dict and primary_color in color_dict[string[i]]):
        if (last_pos != i - 1):
          min_strokes += 1
        last_pos = i
    strokes += min_strokes
  return strokes
def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the Witch's expression
    string_count = input()
    string = input()
    answer = get_number_of_strokes(string)
    print(f'Case #{t+1}: {answer}')
if __name__ == '__main__':
  main()