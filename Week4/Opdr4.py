def F(n):
    m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    y = len(m)-1
    array = []
    insertarray = [0] * int(n + 1)
    insertarray[0] = 1
    for coin in range(0, y):
        if m[coin] < n:
            for amount in range(0, int(n+1)):
                if amount >= m[coin]:
                    insertarray[amount] += insertarray[amount - m[coin]]
            array.append(insertarray[:])
    return array
a = F(12)


for temp in a:
    print(temp)