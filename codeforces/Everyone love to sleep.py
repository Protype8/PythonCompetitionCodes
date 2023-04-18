def main():
  # Get number of test cases
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    number_of_alarm,sleep_hour,sleep_minutes = [int(i) for i in input().split(" ")]
    slept_hour = 100000
    slept_minute = 100000
    for _ in range(number_of_alarm):
      alarm_hour,alarm_minute = [int(i) for i in input("").split(" ")]
      const = 0
      if(alarm_minute < sleep_minutes):
        cur_slept_minutes = (60-sleep_minutes)+alarm_minute
        const = 1
      else:
        cur_slept_minutes = alarm_minute-sleep_minutes
      if(alarm_hour < sleep_hour+const):
        cur_slept_hour = (24-(sleep_hour+const))+alarm_hour
      else:
        cur_slept_hour = alarm_hour-(sleep_hour+const)
      if(cur_slept_hour < slept_hour):
        slept_hour = cur_slept_hour
        slept_minute = cur_slept_minutes
      elif(cur_slept_hour == slept_hour and cur_slept_minutes < slept_minute):
        slept_minute = cur_slept_minutes
    print(slept_hour,slept_minute)
if __name__ == "__main__":
  main()