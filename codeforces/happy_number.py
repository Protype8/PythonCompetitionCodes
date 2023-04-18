import time
def isHappy(n: int) -> bool:
  count = 0
  while n != 1:
    old_num = n
    n = 0
    while old_num > 0:
      n += ((old_num % 10)** 2)
      old_num = old_num // 10
    print(n)
isHappy(19)