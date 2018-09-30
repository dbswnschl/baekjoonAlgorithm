inputString = list(input())
counter69 = 0
arr = []
for i in range(10):
    arr.append(0)
for i in range(len(inputString)):
    inputString[i] = int(inputString[i])
    arr[inputString[i]-1] += 1
if arr.index(max(arr)) == 5 or arr.index(max(arr)) == 8:
    counter69 = arr[5] + arr[8]
    if counter69 %2 == 0:
        arr[arr.index(max(arr))] = int(counter69 / 2)
    else:
        arr[arr.index(max(arr))] = int(counter69/2) +1
print(max(arr))




