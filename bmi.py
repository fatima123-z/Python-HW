height = int(input("enter height:"))
weight = int(input("enter weigt:"))
bmi =weight/(height/100)**2

if bmi< 18.5:
    print("under weight")

elif 18.5 < bmi > 24.9:
    print("normal weight")

elif 25 < bmi > 29.9:
    print("over weight")

elif 30 < bmi > 34.9:
    print("obsity Class I")

elif 35 < bmi > 39.9:
    print("obsity Class II")

elif bmi >= 40:
    print("obsity Class III")

