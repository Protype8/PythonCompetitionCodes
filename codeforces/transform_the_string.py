import string as s
def get_number_of_opreations(string,favorite_words):
  total_opreations = 0
  for letter in string:
    letter_index =s.ascii_lowercase.index(letter)
    for i in range(26):
      if(s.ascii_lowercase[(letter_index+i)%26] in favorite_words):
        total_opreations += i
        break
      letter_index += 26 if letter_index < i else 0
      if(s.ascii_lowercase[(letter_index-i)%26] in favorite_words):
        total_opreations += i
        break
  return total_opreations
def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the Witch's expression
    string = input()
    favorite_words = input()
    answer = get_number_of_opreations(string,favorite_words)
    print(f'Case #{t+1}: {answer}')
if __name__ == '__main__':
  main()