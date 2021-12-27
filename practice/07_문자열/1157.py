S = input().upper()
L = list(set(S))
Z = []

for i in L:
  count = S.count(i)
  Z.append(count)


if Z.count(max(Z))>1:
  print("?")
else:
  max_index = Z.index(max(Z))
  print(L[max_index])