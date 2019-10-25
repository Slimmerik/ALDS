def check(a,i): # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or
    # niet in dezelfde kolom
    i+n in [a[j]+j for j in range(n)] or
    # niet op dezelfde diagonaal
    i-n in [a[j]-j for j in range(n)])
    # niet op dezelfde diagonaal


def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X",end=' ')
            else:
                print("*",end=' ')
        print()
    print()

def rsearch(N):
    global a
    global teller
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a) == N:
                #return True # geschikte a gevonden
                print(a)
                printQueens(a)
                teller = teller+1
            else:
                if rsearch(N):
                    return True
            del a[-1] # verwijder laatste element
    return False

a = [] # a geeft voor iedere rij de kolompositie aan
t = 0
teller = 0
rsearch(8)
print(teller)
#print(a)
#printQueens(a)
