for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    f = 1
    while(x <= M*N):
        if x%N == y%N:
            print(x)
            f = 0
            break
        x += M
    if f:
        print(-1)


# 수학문제 너무 어려움,,, 그냥 이거는 구글링함