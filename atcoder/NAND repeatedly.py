S = input("")
N = len(S)
A = [int(ch) for ch in S]
C = [0] * (N+1)  # Cumulative sum array
total_sum = 0

# Calculate cumulative sum array
for i in range(1, N+1):
    C[i] = C[i-1] + A[i-1]

# Calculate the sum of OR operations for each subarray
for i in range(1, N+1):
    for j in range(i, N+1):
        subarray_sum = C[j] ^ C[i-1]  # XOR of cumulative sums
        total_sum += subarray_sum
print(total_sum)