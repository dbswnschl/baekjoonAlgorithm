inputString = input().split()
for i in range(3):
    inputString[i] = int(inputString[i])

inputString.remove(max(inputString))
print(max(inputString))