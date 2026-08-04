hours=int(input("Enter total working hours= "))

rate=500
overtime_rate=700

if(hours>8):
    overtime=hours-8
    salary=(8*rate) + (overtime*overtime_rate)

    print("Overtime pay Applied!! Total salary= ",salary)
    print("Overtime hours = ",overtime)
else:
    salary=hours*rate
    print("Regular pay = ",salary)
