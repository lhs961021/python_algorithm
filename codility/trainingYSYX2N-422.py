# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    z = (Y-X)//D
    if (Y-X)%D==0:
        return z
    else:
        return z+1