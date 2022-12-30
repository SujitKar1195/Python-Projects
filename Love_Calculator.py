import random

yourName = input("Your Name : ")
aName = input("Your partner's Name : ")

x = random.randint(0, 100)

print(yourName.capitalize(), " ❤️ ", aName.capitalize(), " = "+str(x)+"%")
