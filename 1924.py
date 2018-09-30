inputString = input().split()
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
month31 = [1,3,5,7,8,10,12]
month30 = [4,6,9,11]
month28 = [2]
total = 0
for i in range(len(inputString)):
    inputString[i] = int(inputString[i])
for i in range(inputString[0] - 1):
    if i+1 in month31:
        total += 31
    elif i+1 in month30:
        total += 30
    elif i+1 in month28:
        total += 28
total += inputString[1]
print(day[total%7])




