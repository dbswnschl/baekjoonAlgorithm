testCase = int(input())
for T in range(testCase):
    inputString = input().split()
    M = int(inputString[0])
    N = int(inputString[1])
    x = int(inputString[2])
    y = int(inputString[3])
    count = 1
    year = [1,1] # init
    for i in range(M*N):
        if year == [x,y]:
            break
        elif year == [M,N]:
            count = -1
            break
        if year[0] == M:
            year[0] = 1
        else:
            year[0] += 1
        if year[1] == N:
            year[1] = 1
        else:
            year[1] += 1
        count+=1
    if count >= M*N:
        count = -1
    print(count)








