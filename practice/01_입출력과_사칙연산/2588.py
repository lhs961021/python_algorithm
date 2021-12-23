i = int(input())
j = int(input())

A = i//100
B = (i-(A*100))//10
C = (i-(A*100)-(B*10))
D = j//100
E = (j-(D*100))//10
F = (j-(D*100)-(E*10))

print(i*F)
print(i*E)
print(i*D)
print(i*j)