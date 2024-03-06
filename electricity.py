unit = float("Input Electrical unit charges")
if(unit <= 50):
    print(amt = unit * 0.50)
elif(unit <= 150):
     print( amt = 25 + ((unit-50) * 0.75))
elif(unit <=200):
     print(amt = 100 + ((unit-150) * 1.20))  
else:
     print(amt = 220 + ((unit-250) * 1.50))  

total = amt * 0.20