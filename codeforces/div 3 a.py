def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    input("")
    cat = input("").lower()
    out = ""
    current = ""
    for i in range(len(cat)):
      if(cat[i] != current):
        current = cat[i]
        out += current
    if(out == "meow"):
      print("Yes")
    else:
      print("No")
if __name__ == "__main__":
  main()