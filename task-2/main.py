from mod import guessNumber
import random

computerNum = round(random.random()*100)

while True:
    userNum = int(input("Введіть число від 0 до 100: "))
    guessNumber(userNum, computerNum)
    if computerNum == userNum: break