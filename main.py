# create a function that will return the letter grade
# user input
# print
import random
n = random.randint(50, 100)


if n < 60:
    print("F")
elif n < 70:
    print("D")
elif n < 80:
    print("C")
elif n < 90:
    print("B")
elif n <= 100:
    print("A")
print(n)

print("Days in this program will be represented by a number.")
print("Sunday - Saturday will be the digits 0 - 6.")
beginning_day = input("Enter beginning day (0 - 6) :")
absent_days = input("How many days will you be gone? ")
coming_home = random.randint(0, 6)
if coming_home < 0:
    print("Sunday")
elif coming_home < 1:
    print("Monday")
elif coming_home < 2:
    print("Tuesday")
elif coming_home < 3:
    print("Wednesday")
elif coming_home < 4:
    print("Thursday")
elif coming_home < 5:
    print("Friday")
elif coming_home < 6:
    print("Saturday")

startLocation = int(input("Enter starting location: "))
diceRoll = int(input("Enter dice roll: "))
endLocation = startLocation + diceRoll
print("Your ending location is:", endLocation)
if endLocation > 27:
    print("Your ending location is:", endLocation - 5)

transactionAmount = int(input("Enter starting location: "))
amountPaid = int(input("Enter starting location: "))
changeDue = amountPaid - transactionAmount
bill1 = changeDue/20.0
bill2 = bill1/10.0
bill3 = bill2/5.0
bill4 = bill3/.5
print("Change due is", changeDue)
print("You need", bill1, bill2, bill3, bill4)
