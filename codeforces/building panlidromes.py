def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    N, Q = map(int, input().split())
    blocks = input()
    questions = []
    for i in range(Q):
      L, R = map(int, input().split())
      questions.append((L, R))
    answer = count_yes(N, Q, blocks, questions)
    print(f'Case #{test_case}: {answer}')
def count_yes(N, Q, blocks, questions):
  answer_dict = {}
  word_dict_list = [{word:0 for word in set(list(blocks))}]
  for block in blocks:
    new_dict  =word_dict_list[-1].copy()
    new_dict[block] += 1
    word_dict_list.append(new_dict)
  # TODO: Complete this function and return the number of "yes" answers.
  yes_answers = 0
  for question in questions:
    if(question in answer_dict):
      yes_answers += answer_dict[question]
    else:
      odd_encountered = False
      L,R = question[0]-1,question[1]
      for word,right_word_count in word_dict_list[R].items():
        if((right_word_count-word_dict_list[L][word])%2 != 0):
          if(odd_encountered):
            answer_dict[question] = 0
            break
          odd_encountered = True

      else:
        answer_dict[question] = 1
        yes_answers += 1
  return yes_answers
if __name__ == '__main__':
  main()