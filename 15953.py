

T = int(input().split()[0])

arr_2017 = [0]
arr_2018 = [0]
money_2017 = [500,300,200,50,30,10]
money_2018 = [512,256,128,64,32]
for i in range(6):
    for j in range(i+1):
        arr_2017.append(money_2017[i])

for i in range(5):
    for j in range(pow(2,i)):
        arr_2018.append(money_2018[i])
result = ""
for aaaa in range(T):
    txt = input()
    a = int(txt.split(" ")[0])
    b = int(txt.split(" ")[1])
    if a>21:
        a = 0
    if b > 31:
        b = 0

    result += str((arr_2017[a]+arr_2018[b])*10000)+"\n"
print(result,end="")
