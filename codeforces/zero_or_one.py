test_cases = int(input(""))
for i in range(test_cases):
  n = int(input(""))
  if(n == 2):
    print(1)
  else:
    ans = 2
    for b in range(3,n):
      copy_n = n
      while(copy_n):
        remainder = copy_n%b
        if(remainder != 0 and remainder != 1):
          break
        copy_n //= b
      else:
        ans += 1
    print(ans)