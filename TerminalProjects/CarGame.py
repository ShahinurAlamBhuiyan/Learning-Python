command = ""
isCarStart = False
while True:
    command = (input(">")).lower()
    if command == 'help':
        print("""start - to start the car .
stop - to stop the car.
quit - to exit.""")
    elif command == 'start':
        if not isCarStart:
            isCarStart = True
            print("Car stared... Ready to go!")
        else:
            print("Car is already started!")
    elif command == 'stop':
        if isCarStart:
            isCarStart = False
            print("Car stopped.")
        else:
            print("Car is already stopped!")

    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand!")
