T = int(input(""))
for _ in range(T):
  n,d,h = [float(i) for i in input("").split(" ")]
  n = int(n)
  d_to_h_ratio = d/h
  bases = [float(i) for i in input("").split(" ")]
  area = 0.5*d*h
  for i in range(n-2,-1,-1):
    covered_height = bases[i]+h-bases[i+1]
    area += 0.5*d*h
    if(covered_height > 0):
      covered_base = d_to_h_ratio*covered_height
      area -= 0.5*covered_base*covered_height
  print(area)