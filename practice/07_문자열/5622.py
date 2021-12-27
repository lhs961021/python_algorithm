S = list(input())
sum = 0
a = 0

for i in S:
  if i in ['A','B','C']:
    sum += 3
  elif i in ['D','E','F']:
    sum += 4
  elif i in ['G','H','I']:
    sum += 5
  elif i in ['J','K','L']:
    sum += 6
  elif i in ['M','N','O']:
    sum += 7
  elif i in ['P','Q','R','S']:
    sum += 8
  elif i in ['T','U','V']:
    sum += 9
  else:
    sum += 10


print(sum)
