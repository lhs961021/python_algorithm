import sys

def finder(answer):
  if ('()' in answer) or ('[]' in answer):
    answer = answer.replace("()","")
    answer = answer.replace("[]","")
    finder(answer)
  else:
    if ('(' in answer) or (')' in answer) or ('[' in answer) or (']' in answer):
      print("no")
    else:
      print("yes")


while True:

  A = list(str(sys.stdin.readline().rstrip()))

  data = []

  if A[0]==".":
    break
  
  for i in A: 
    if i=='[' or i==']' or i=='(' or i==')':
      data.append(i)

  if len(data)==0:
    print("yes")
  else:
    answer="".join(data)

    finder(answer)