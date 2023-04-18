def get_changes(x,a):
  lower_bound = a[0]-x
  upper_bound = x+a[0]
  changes = 0
  counter = 1
  while counter < len(a):
    if(abs(a[counter]-lower_bound) <= x or abs(a[counter]-upper_bound) <= x):
      if(lower_bound <= a[counter] <= upper_bound):
        lower_bound = max(a[counter]-x,lower_bound)
        upper_bound = min(a[counter]+x,upper_bound)
      #if upper is closer than lower
      else:
        if(abs(a[counter]-lower_bound) > abs(a[counter]-upper_bound)):
          lower_bound = upper_bound - abs(a[counter]-upper_bound)
        elif(abs(a[counter]-lower_bound) < abs(a[counter]-upper_bound)):
          upper_bound = lower_bound + abs(a[counter]-lower_bound)
    else:
      changes+=1
      lower_bound = abs(x - a[counter])
      upper_bound = abs(x + a[counter])
    counter += 1
  return changes
def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    _,x = input().split(" ")
    a = [int(i) for i in input().split(" ")]
    print(get_changes(int(x),a))
if __name__ == "__main__":
  main()