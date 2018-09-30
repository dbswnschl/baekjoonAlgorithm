inputValue = int(input())

for i in range(inputValue,0,-1):
    for j in range(inputValue-1,inputValue-i-1,-1):
        print("*",end="")
    print("")