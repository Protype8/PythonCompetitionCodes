all_dict = [{}]
d = {}
s = input("")
for c in s:
  d[c] = d.get(c,0)+1
  all_dict.append(d.copy())
count = 0
for i in range(len(s)+1):
  for j in range(i+1,len(s)+1):
    for key in all_dict[j]:
      a = all_dict[j][key] - all_dict[i].get(key,0)
      if(a%2 != 0):
        break
    else:
      count += 1
print(count)