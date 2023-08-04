N = int(input(""))
A = [int(i) for i in input().split(" ")]
Fa = [0]
for i in range(1,len(A)):
  if(i%2 == 0):
    Fa.append(Fa[-1]+A[i]-A[i-1])
  else:
    Fa.append(Fa[-1])
def binary_search(to_search):
  left = 0
  right = len(A)
  while (left <= right):
    mid = (right+left)//2
    if (A[mid] > to_search):
      right = mid - 1
    elif(A[mid] < to_search):
      left = mid + 1
    else:
      return mid
  return right
def F(closet,x):
  if(closet+1 == len(A)):
    return Fa[closet]
  return Fa[closet]+(x-A[closet])*((Fa[closet+1]-Fa[closet])/(A[closet+1]-A[closet]))
Q = int(input(""))
for _ in range(Q):
  left_val,right_val = [int(i) for i in input().split(" ")]
  left_index = binary_search(left_val)
  right_index = binary_search(right_val)
  print(int(F(right_index,right_val)-F(left_index,left_val)))