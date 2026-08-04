value1=int(input("Enter first value: "))
value2=int(input("Enter second value: "))
operator=input("Enter operator: ")

match operator:
    case "+":
        print("Sum = ",value1+value2)
    case "-":
        print("Difference = ",value1-value2) 
    case "*":
        print("Multiplication = ",value1*value2)
    case "/":
        print("Division = ",value1/value2)
    case _:
        print("Invalid operator!")            