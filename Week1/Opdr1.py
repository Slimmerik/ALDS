a = [45,65,34,82,30,22]
b = [45,'sdf',34,82,30,22]
c = []
print('a: ', a)

def mymax(a):
    b = 0
    try:
        assert len(a) > 0;
        for t in a:
            assert isinstance(t,int)
            if (t > b):
                b = t

        return b
    except AssertionError:
        print ("Lijst is leeg of de lijst bestaat niet alleen uit cijfers")

print(mymax(a))
print(mymax(b))
print(mymax(c))