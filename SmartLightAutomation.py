time=int(input("Enter time in 24-format(0-24): "))

if time>=18 or time<=6:
    print("Turn On Lights.")
else:
    print("Turn Off Lights.")
