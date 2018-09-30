inputArr = list(input())
length = len(inputArr)
count = 0
for i in range(0,length,1 ):
    if i != 0 and i % 10 == 0:
        print("")
    print(inputArr[i],end="")
