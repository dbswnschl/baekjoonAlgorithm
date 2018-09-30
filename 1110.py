# 1.
# N < 10 --> "0N" --> 0+N
# N > 10 --> N의 각 자리수를 더함
# 2.
# 가장 오른쪽자리숫자와 1.의 합의 가장 오른쪽 숫자를 이어붙임

def cycle(num):
    num10 = int(num / 10) # 6
    num1 = num - num10 * 10 # 8
    sum10 = int((num10 + num1) / 10)
    sum1 = num10 + num1 - sum10*10
    sum = (num1 * 10) + sum1  # 80 + 4
    return sum


inputValue = int(input())
count = 0
i = inputValue
while(True):
    i = cycle(i)
    count+=1
    if i == inputValue:
        break
print(count)

