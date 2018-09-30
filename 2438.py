import numpy as np

inputValue = int(input())
for i in range(inputValue):
    for j in range(i+1):
        print("*",end="")
    print("")
