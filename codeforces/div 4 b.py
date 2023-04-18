def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    cur_x = cur_y = 0
    direction_dict = {"L":(-1,0),"R":(1,0),"U":(0,1),"D":(0,-1)}
    words = input("")
    directions = input("")
    for dir in directions:
      change_x,change_y = direction_dict[dir]
      cur_x += change_x
      cur_y += change_y
      if(cur_x == 1 and cur_y == 1):
        print("YES")
        break
    else:
      print("NO")
if __name__ == "__main__":
  main()