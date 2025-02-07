member = int(input("1.Gold, 2.Silver,3.Normal"))
if member == 1:
    print("above one hundred,")
    amount = float (input("enter spending:"))
    if amount > 100:
      print(amount * .1)
    else:
       print(amount * .1)
if member == 2:
   print(" and also above one hundred,") 
   amount = float (input("enter spending:"))
   if amount > 100:
       print(amount * .15)
else:
    print(amount * .5)
if member == 3:
    print("but not above one hundred,")
    amount = float (input("enter spending"))
    if amount >100:
       print(amount * .05)
    else:
       print(amount * .0)
       
      
            

    