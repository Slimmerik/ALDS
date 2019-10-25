
dict = {}

deelwaarden = 1

print(repr(2**32))

while True:
    deelwaarden+=1
    waardenn = 1/deelwaarden
    waarden = hash(waardenn)%100000000

    for x,y in dict.items():
        if y == waarden:
            print("match#: " + str(repr(waardenn)) + " " + str(x) + " -> " + str(repr(y)) + " " + str(waarden))
    dict[waardenn] = waarden

