def computepay(h, r):
    if h > 40:
        extra = h - 40
        mp = 40*r
        xp = extra * r * 1.5
        pay = mp + xp
        return pay
    else:
        pay = r*h
        return pay


hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
p = computepay(hrs, rate)
print("Pay", p)
