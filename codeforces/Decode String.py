import string
def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    length = int(input(""))
    code = input("")
    counter = length-1
    decode = ""
    while counter >= 0:
      if(code[counter] != "0"):
        decode = string.ascii_lowercase[int(code[counter])-1] + decode
        counter -= 1
      else:
        decode = string.ascii_lowercase[int(code[counter-2:counter])-1]+decode
        counter -= 3
    print(decode)
if __name__ == "__main__":
  main()