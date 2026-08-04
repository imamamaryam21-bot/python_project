command=input("Enter a command (start,stop,restart): ")

match command.lower():
    case "start":
        print("System is going to start....")
    case "stop":
        print("System is shutting down....")
    case "restart":
        print("System restarting....")
    case _:
        print("Unknown command!")
        