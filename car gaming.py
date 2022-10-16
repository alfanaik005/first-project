#car gaming
command = ""
started = False
while True:
    command = input('> ').lower()
    if command == 'help':
        print("""start - car is started
stop - car is stopped
quit - exist""")
    elif command == 'start':
        if started:
            print("car is already started!")
        else:
            started = True
            print("car is started...")
    elif command == 'stop':
        if not started:
            print("need to start the car first")
        else:
            started = False
            print("car is stopped")
    elif command == 'quit':
        break
    else:
        print("oops! erorr")


