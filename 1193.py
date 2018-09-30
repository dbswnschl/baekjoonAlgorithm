

inputValue = int(input())


count = 0
i = 1
plusMinus=False # Minus Start
result = 1



def startEnd(start,end,src,dest):
    cnt = src
    if start < end:
        for i in range(start,end+1):
            cnt +=1
            if cnt == dest:
                print(i,end="")
                break
    else:
        for i in range(start,end-1,-1):
            cnt +=1
            if cnt == dest:
                print(i,end="")
                break
    return cnt

while(True):
    if i % 2 == 1:
        count = startEnd(i,1,count,inputValue)
    else:
        count = startEnd(1,i,count,inputValue)
    if count == inputValue:
        break
    i +=1
print("/",end="")
count = 0
i=1
while(True):
    if i % 2 == 0:
        count = startEnd(i,1,count,inputValue)
    else:
        count = startEnd(1,i,count,inputValue)
    if count == inputValue:
        break
    i+=1

# 1번 1
# 2번 1 2
# 3번 3 2 1
# 4번 1 2 3 4
# 5번 5 4 3 2 1
#
#
#
#
#
