import math
import random

def calculateZ (m, n):
    z = (math.sqrt(2) - math.sqrt(3*n))/(2 * m)
    return z

def guessNumber (userNum, computerNum):
    if userNum < computerNum: print("Моє число більше")
    elif userNum > computerNum: print("Моє число менше")
    else: print("Ви вгадали")

m = int(input("Введіть число m: "))
n = int(input("Введіть число n: "))

print("Результат обчислення числа z =", calculateZ(m, n))

computerNum = round(random.random()*100)

while True:
    userNum = int(input("Введіть число від 0 до 100: "))
    guessNumber(userNum, computerNum)
    if computerNum == userNum: break