def machtv3(a,n):
    assert n > 0
    teller = 0
    m = 1
    while n > 0:
        if n%2 == 0:
            teller = teller +1
            m = m * a**2
            n = n -2
        else:
            teller = teller +1
            n = n -1
            m = m * a
    print(teller)
    return m

print(machtv3(2, 5000))