import numpy as np
testCase = int(input())

# def calc(k,n):
#     if n == 1:
#         return 1
#     if k == 0:
#         return n
#     return calc(k-1,n) + calc(k,n-1)
#
#
# def calc(k,n):
#     if k == 0:
#         return n
#     elif n == 1:
#         return 1
#     # 상수 + 변수 모형
#     #1. 0층 n호
#     #층수별 n-1호
#     result = n
#     for i in range(k):
#         result += calc(i+1,n-1)
#     return result
#
arr = [[0 for col in range(1000)] for row in range(1000)]
#init
for i in range(0,15,1): #0층 ~ 14층
    for j in range(1,15,1): #1호 ~ 14호
        if i == 0:
            arr[i][j] = j
        elif j == 1:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]


result = []
for T in range(testCase):
    k = int(input())
    n = int(input())
    result.append(arr[k][n])
for i in result:
    print(i)

