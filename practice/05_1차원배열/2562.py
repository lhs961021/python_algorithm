data = []

for j in range(0,9):
    data.append(int(input()))

i = max(data)
a = data.index(i)+1
print(i)
print(a)
