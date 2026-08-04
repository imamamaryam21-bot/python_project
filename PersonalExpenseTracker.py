print("---Welcome to personal Expense tracker---")

food=0.0
transport=0.0
bills=0.0
shopping=0.0
others=0.0
total=0.0

while True:
    print("\nChoose an option: ")
    print("1. Add expense")
    print("2. show summary")
    print("3. Data export")
    print("4. Exit")

    choice=input("Enter your choice: ")
    match choice:
        case "1":
            print("\nCategories: food,transport,bills,shopping,others")
            category=input("Enter category: ").lower()
            amount=float(input("Enter amount: "))

            if category=="food":
                food+=amount
            elif category=="transport":
                transport+=amount
            elif category=="bills":
                bills+=amount
            elif category=="shopping":
                shopping+=amount
            else:
                others+=amount

            total=food+transport+bills+shopping+others
            print("Added", amount ,"to", category ,"category") 

        case "2":
            print("show summary")
            print("Food: ",food)
            print("Transport: ",transport)
            print("Bills: ",bills)
            print("Shopping: ",shopping)
            print("Others: ",others)
            print("Total: ",total)

            if total>100000:
                print("Warning! You have spent more than one lac this month.")
            elif total==0:
                print("You have not added any expense yet.")    
            else:
                print("You are managing your budget wisely.")    
        case "3":
            print("Data Export")        

        case "4":
            print("Exit....")    
            break
        case _:
            print("Invalid input.")                     