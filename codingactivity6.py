import random
n = random.randint(0, 20)
for wedgeOfStars in range(n, 0, -1):
    for j in range(0, wedgeOfStars):
        print("*", end=" ")
print()
