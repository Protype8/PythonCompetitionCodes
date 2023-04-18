cases = int(input(""))
for case in range(cases):
    _,no_of_kids = input("").split(" ")
    no_of_kids = int(no_of_kids)
    bag_list = [int(i) for i in input("").split(" ")]
    candy_for_each_child = int(sum(bag_list)/no_of_kids)
    left_over_candies = sum(bag_list)-candy_for_each_child*no_of_kids
    print(f"Case #{case + 1}: {left_over_candies}")