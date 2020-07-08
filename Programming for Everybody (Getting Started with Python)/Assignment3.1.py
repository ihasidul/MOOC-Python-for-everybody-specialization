hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate per hour: ")
rph = float(rph)

if h > 40:
    extra = h - 40
    mp = 40*rph
    xp = extra * rph * 1.5
    pay = mp + xp
    print(pay)
else:
    pay = rph*h
    print(pay)
