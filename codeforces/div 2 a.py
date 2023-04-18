def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    a,b = [int(i) for i in input().split(" ")]
    n,m = [int(i) for i in input().split(" ")]
    amount_of_buyable_ones = n//(m+1)
    cost = a*(amount_of_buyable_ones*m)
    left = n-(amount_of_buyable_ones*(m+1))
    if(left > 0):
      cost += (min(a,b)*left)
    cost = min(cost,b*n)
    print(cost)
if __name__ == "__main__":
  main()