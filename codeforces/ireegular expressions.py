# TODO: Complete the check_spell function
from functools import reduce
def find_indices(list_to_check, item_to_find):
  return [idx for idx, value in enumerate(list_to_check) if value == item_to_find]
def get_count_of_vowel(expression):
  vowels = ["a", "e", "i", "o", "u"]
  return sum([expression.count(vowel) for vowel in vowels])
def check_spell(expression):
  #Finding first and last word
  #first word need to be at least 4 words long to contain 2 syllables
  current_length = 4
  first_and_last_word = ""

  for i in range(len(expression)-3):
    # middle word is at least 2 words and first word can only as long as half the expression
    max_length = int((len(expression)-i) - 2) / 2
    if(max_length < current_length):
      break
    while 1:
      if(expression[i:].count(expression[i:i+current_length]) >= 2):
        first_and_last_word = expression[i:i+current_length]
        distance_of_last_word_from_first_word = expression[i+current_length:].index(first_and_last_word)
        if(distance_of_last_word_from_first_word < 2):
          current_length -= 1
          break
        if(current_length < max_length):
          current_length += 1
        else:
          break
      else:
        if(current_length > 4):
          current_length-=1
        break
  #check if the first and last word have 2 syabbles
  vowel_index_list = []
  for vowel in vowels:
    vowel_index_list += find_indices(list(first_and_last_word),vowel)
  if(len(vowel_index_list) == 2 and abs(reduce(lambda x, y: x - y, vowel_index_list)) > 1):
    #check if middle word is a syabble
    word_list = expression.split(first_and_last_word)
    #middle word is in the middle...
    middle_word = word_list[int(len(word_list)/2)]
    #middle word contain at least one vowel to make it a syllable
    if(sum([middle_word.count(vowel) for vowel in vowels]) == 1):
      return True
  return  False
def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the Witch's expression
    expression = input()
    answer = 'Nothing.'
    if(check_spell(expression)):
      answer = 'Spell!'
    print(f'Case #{t+1}: {answer}')

if __name__ == '__main__':
  main()


