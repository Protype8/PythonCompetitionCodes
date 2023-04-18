
def check_spell(expression):
  vowels = ["a", "e", "i", "o", "u"]
  for i in range(len(expression)):
    current_vowels = []
    for j in range(i,len(expression)):
      if(expression[j] in vowels):
        current_vowels.append(j)
        if(len(current_vowels) == 3):
          start = expression[current_vowels[0]:current_vowels[1]+1]
          rest_of_spell = expression[current_vowels[2]+1:]
          if(start in rest_of_spell):
            return True
          break
  return False
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


