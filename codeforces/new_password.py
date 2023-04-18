import string
speical_characters = ["#", "@", "*", "&"]
def get_new_password(old_password):
  requirements = [string.ascii_uppercase,string.ascii_lowercase,string.digits,speical_characters]
  placed = [False,False,False,False,False]
  add_on = ""
  for requirement in requirements:
    contain = False
    for word in old_password:
      if(word in requirement):
        contain = True
        break
    if(not contain):
      if (placed[requirements.index(requirement)] == False):
        add_on += requirement[0]
        placed[requirements.index(requirement)] = True
  while (len(old_password+add_on) < 7):
    add_on += "1"
  return old_password+add_on
def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the Witch's expression
    _ = input()
    old_password = input()
    answer = get_new_password(old_password)
    print(f'Case #{t+1}: {answer}')
if __name__ == '__main__':
  main()


