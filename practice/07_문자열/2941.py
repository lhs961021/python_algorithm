S = input()
z = ['c=','c-','dz=','d-','lj','nj','s=','z=']

sum = 0

for i in z:
  if S.count(i)>0:
    sum+=S.count(i)
    S = S.replace(i," ")

S = ' '.join(S).split()

print(sum+len(S))