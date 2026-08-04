print("----Monthly Expense Tracker----")
rent=float(input("Enter your house rent: "))
groceries=float(input("Enter groceries expense: "))
transport=float(input("Enter transport expense: "))
utility=float(input("Enter your utility bills: "))

total=rent+groceries+transport+utility

income=float(input("\nEnter your Monthly income: "))

if(total>income):
    print("Warning!! You are over spending.")
elif(total==income):
    print("You are breaking over!!")
else:
    savings=income-total
    print("Good job! You saved Rs. ",savings)

