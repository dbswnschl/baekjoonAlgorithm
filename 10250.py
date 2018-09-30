



testCase = int(input())

for T in range(testCase):
    inputString = input().split()
    H = int(inputString[0])
    W = int(inputString[1])
    N = int(inputString[2])
    if N%H == 0:
        print(H,end="")

    else:
        print(N%(H),end="")
    XX = int(N/(H))+1
    if N%H == 0:
        XX-=1

    if XX<10:
        print("0",end="")
    print(XX)