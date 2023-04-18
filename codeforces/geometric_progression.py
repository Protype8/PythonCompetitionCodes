A,X,M = [int(i) for i in input().split(" ")]
sum =0
for i in range(X):
  sum += pow(A,i,M)
print(sum)