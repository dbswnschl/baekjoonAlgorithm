
inputValue = int(input())

# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력
# 한수란, 자리수가 등차수열을 이루는것

def calc(num):
    num100 = int(num / 100)
    num10 = int((num - num100*100) / 10)
    num1 = int(num- (num100*100+num10*10))
    if num100 > 0:
        if num100 - num10 == num10 - num1:
            return True
        else:
            return False
    else:
        return True
count = 0

for i in range(inputValue):
#   i가 한수이면 count += 1
    if calc(i+1) == True:
        count+=1
print(count)
