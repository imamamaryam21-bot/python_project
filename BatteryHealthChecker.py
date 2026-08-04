battery=int(input("Enter your phone battery: "))

if battery>=80:
    print("You can plug out the charger.")
elif battery>=50:
    print("Normal battery...keep charging!")
else:
    print("Warning! Low battery.")