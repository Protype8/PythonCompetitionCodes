length = int(input(""))
called = [False for i in range(length)]
arr = [int(i) for i in input().split(" ")]
for i in range(length):
  if(not called[i]):
    called[arr[i]-1] = True
not_called_arr = []
for i in range(length):
  if(not called[i]):
    not_called_arr.append(str(i+1))
print(len(not_called_arr))
print(" ".join(not_called_arr))