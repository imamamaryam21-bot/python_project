device=input("Enter device name: ")

match device.lower():
    case "fan":
        print("Turn ON fan.")
    case "light":
        print("Turn ON lights.")
    case "AC":
        print("Starting AC")
    case _:
        print("Device not recognized!")            