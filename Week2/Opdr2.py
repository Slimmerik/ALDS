class stack():

    def __init__(self):
        self.a = []

    def POP(self):
        return self.a.pop()

    def PUSH(self, topush):
        self.a.append(topush)


    def PEEK(self, i):
        return self.a[i]

    def is_empty(self):
        boolTmep = False
        if(len(self.a) == 0):
            boolTmep = True
        return boolTmep


stck = stack()

print(stck.is_empty())
stck.PUSH(1)
stck.PUSH(2)
stck.PUSH(3)
stck.PUSH(4)
print(stck.PEEK(2))
print(stck.POP())
print(stck.POP())
print(stck.is_empty())