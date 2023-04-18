def get_medium_of_list(list):
  median = len(list)//2
  if(len(list)%2 == 0):
    return (list[median]+list[median-1])/2
  else:
    return list[median]
def main():
  test_cases = int(input(""))
  for i in range(test_cases):
    number_of_regions,number_of_categories = [int(i) for i in input("").split(" ")]
    number_list = [int(i) for i in input("").split(" ")]
    number_list.sort(reverse=True)
    categories = []
    meidans = []
    counter = 0
    for number in number_list:
      if counter < number_of_categories:
        categories.append([number])
        meidans.append(number)
      else:
        index = meidans.index(min(meidans))
        categories[index].append(number)
        meidans[index] = get_medium_of_list(categories[index])
      counter += 1
    print(f"Case #{i+1}: {sum(meidans)}")
if __name__ == "__main__":
  main()