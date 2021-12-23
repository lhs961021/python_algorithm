data = []
answer = []
answer_1 = {}

for _ in range(10):
  data.append(int(input())) 

for i in data:
  a = i % 42
  answer.append(int(a))

for i in answer:
  try: answer_1[i] += 1
  except: answer_1[i] = 1

print(len(answer_1.keys()))