
inputValue = int(input())
inputString= input().split()
for i in range(inputValue):
    inputString[i] = int(inputString[i])
M = max(inputString)
indexM = inputString.index(M)
total = 0
for i in range(inputValue):
    inputString[i] = inputString[i] / M * 100
    total += inputString[i]
print(round(total / inputValue,2))

