import math
n = int(input(""))
station_at_back = math.floor(n/5)*5
station_at_front = math.ceil(n/5)*5
if(n-station_at_back < station_at_front-n):
  print(station_at_back)
else:
  print(station_at_front)