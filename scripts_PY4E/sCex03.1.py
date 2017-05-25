hrs = int(raw_input("Hours?: "))
rate = int(raw_input("Rate?: "))

if hrs > 40:
    pay = rate * (40 + ( hrs - 40 ) * 1.5)
    print pay
else:
    pay = rate * hrs
    print pay
