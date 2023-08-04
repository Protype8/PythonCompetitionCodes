N = int(input(""))
def check_if_panlidrome(s):
  for i in range(len(s)):
    if(s[i] != s[len(s)-i-1]):
      return False
  return True
strings = []
for _ in range(N):
  strings.append(input(""))
for i in range(N):
  for j in range(i+1,N):
    if(check_if_panlidrome(strings[i]+strings[j]) or check_if_panlidrome(strings[j]+strings[i])):
      print("Yes")
      break
  else:
    continue
  break
else:
  print("No")
