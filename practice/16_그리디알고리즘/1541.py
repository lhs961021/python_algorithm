arr = input().split('-') 
s = 0 

for i in arr[0].split('+'): 
  s += int(i) 
for i in arr[1:]:
  for j in i.split('+'): 
    s -= int(j) 
print(s)

# 구글링 함 다시 풀어봐야함 
# .split()사용시 나오는 것들을 for 문으로 받을수 있다.