Ha,Wa = [int(i) for i in input("").split(" ")]
A = []
left = Wa
right = bottom = 0
top = Ha
for i in range(Ha):
  a = []
  s = list(input())
  for j in range(Wa):
    if(s[j] == "#"):
      left = min(left,j)
      right = max(right,j)
      top = min(top,i)
      bottom = max(bottom,i)
    a.append(s[j])
  A.append(a)
A = A[top:bottom+1]
for i in range(len(A)):
  A[i] = A[i][left:right+1]
Hb,Wb = [int(i) for i in input("").split(" ")]
B = []
left = Wb
right = bottom = 0
top = Hb
for i in range(Hb):
  b = []
  s = list(input())
  for j in range(Wb):
    if (s[j] == "#"):
      left = min(left, j)
      right = max(right, j)
      top = min(top, i)
      bottom = max(bottom, i)
    b.append(s[j])
  B.append(b)
B = B[top:bottom+1]
for i in range(len(B)):
  B[i] = B[i][left:right+1]
Hx,Wx = [int(i) for i in input("").split(" ")]
valid = False
X = []
for i in range(Hx):
  x = list(input(""))
  X.append(x)
if not (Hx < len(A) or Hx < len(B) or Wx < len(A[0]) or Wx < len(B[0])):
  for i in range(Hx-len(A)+1):
    for j in range(Wx-len(A[0])+1):
      for k in range(Hx-len(B)+1):
        for l in range(Wx-len(B[0])+1):
          c = [['.' for _ in range(Wx)] for _ in range(Hx)]
          for a in range(len(A)):
            for b in range(len(A[0])):
              c[i + a][j + b] = "#" if A[a][b] == "#" else c[i + a][j + b]
          for m in range(len(B)):
            for n in range(len(B[0])):
              c[k + m][l + n] = "#" if B[m][n] == "#" else c[k + m][l + n]
          if(c == X):
            valid = True
if(valid):
  print("Yes")
else:
  print("No")