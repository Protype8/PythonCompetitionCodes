import re
opreations = {"01":"2","12":"3","23":"4","34":"5","45":"6","56":"7","67":"8","78":"9","89":"0","90":"1"}
def get_opreation_result(string):
  result = string
  prev_result = string
  area_of_interest = []
  while 1:
    if(area_of_interest != []):
      for key,value in opreations.items():
        if(key in result):
          for area in area_of_interest:
            if(result[area-1:area] == key):
              result = result[:area-1]+key+result[area+1:]
            elif(result[area:area+1] == key):
              result = result[:area]+key+result[area+2:]
            else:
              area_of_interest.remove(area)
    else:
      for key,value in opreations.items():
        if(key in result):
          area_of_interest += [index.start() for index in re.finditer(pattern=key, string=string)]
          result = result.replace(key,value)
    if(result == prev_result):
      break
    else:
      prev_result = result
  return result
def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the Witch's expression
    string_count = input()
    string = input()
    answer = get_opreation_result(string)
    print(f'Case #{t+1}: {answer}')
if __name__ == '__main__':
  main()