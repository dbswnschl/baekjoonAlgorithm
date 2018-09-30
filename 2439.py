inputValue = int(input())
for j in range(inputValue):
    for k in range(inputValue-j-1,0,-1):
        print(" ",end="")
    for i in range(0,j+1,1):
        print("*",end="")
    print("")