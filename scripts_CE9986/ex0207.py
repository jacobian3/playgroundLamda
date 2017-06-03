while True:
    uin = input("how many times should I greet you? ")
    
    if uin.isdigit():
        count = 1

        while count < int(uin)+1:
            print("Happy birthday to you!","time: {}".format(count))
            count += 1
        exit()

    print("error: please enter an integer")
    
