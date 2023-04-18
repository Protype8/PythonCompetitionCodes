# TODO: Complete the get_minimum_overall_delivery_time function
def get_minimum_overall_delivery_time(rows, columns, grid):
  delivery_list = []
  buildable_list = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if(grid[i][j] == 1):
        delivery_list.append((i,j))
      else:
        buildable_list.append((i,j))
  overall_delivery_time_per_pos = []
  for position in buildable_list:
    temp_buildabe_list = buildable_list.copy()
    temp_delviery_list = delivery_list.copy()
    temp_delviery_list.append(position)
    temp_buildabe_list.remove(position)
    overall_delviery_times = []
    for pos_1 in temp_buildabe_list:
      delivery_time = 10000000000
      for pos_2 in temp_delviery_list:
        new_delivery_time = abs(pos_2[0]-pos_1[0])+abs(pos_2[1]-pos_1[1])
        if(new_delivery_time < delivery_time):
          delivery_time = new_delivery_time
      overall_delviery_times.append(delivery_time)
    if(len(overall_delviery_times) > 0):
      overall_delivery_time_per_pos.append(max(overall_delviery_times))
  # TODO: Add logic to calculate the minimum overall delivery time
  return min(overall_delivery_time_per_pos) if len(overall_delivery_time_per_pos) > 0 else 0
def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the grid dimensions
    rows, columns = map(int, input().split())
    # Get the grid
    grid = [list(map(int, input())) for _ in range(rows)]
    print(f'Case #{t+1}:',
          get_minimum_overall_delivery_time(rows, columns, grid))

if __name__ == '__main__':
  main()
