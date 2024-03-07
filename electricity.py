units = int(input("Enter the number of units consumed: "))

if units <= 50:
    bill = units * 0.5
elif units <= 150:
    bill = 25 + (units - 50) * 0.75
elif units <= 250:
    bill = 25 + 75 + (units - 150) * 1.2
else:
    bill = 25 + 75 + 120 + (units - 250) * 1.5

surcharge = 0.2 * bill
total_bill = bill + surcharge

print("Electricity Bill: Rs.", bill)
print("Surcharge (20%): Rs.", surcharge)
print("Total Bill: Rs.", total_bill)