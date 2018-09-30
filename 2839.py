inputValue = int(input())
#봉지는 3kg, 5kg
count5 = 0
count3 = 0


for i in range(int(inputValue / 5),1,-1):
    if (inputValue - (5 * (i) )) % 3 == 0:
        count5 = i
        break
if count5 != 0:
    count3 = int((inputValue - 5 * count5)/3)
    print(count3 + count5)
elif inputValue % 3 == 0:
    print(int(inputValue / 3))
else:
    print(-1)