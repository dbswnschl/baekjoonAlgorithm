inputValue = int(input())

for i in range(inputValue):
    for j in range(i):
        print(" ",end="")
    for k in range(inputValue - i,0,-1):
        print("*",end="")
    print("")
