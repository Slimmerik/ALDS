string1 = '((<>)())'
string2 = '[(<>)]( )(( )( ))'
string3 = '((<>))'
string4 = '((( < ) >))'
string5 = '( [ )]'

class stack():

    def __init__(self):
        self.a = []

    def POP(self):
        return self.a.pop()

    def PUSH(self, topush):
        self.a.append(topush)


    def PEEK(self, i):
        return self.a[i]

    def PEEK_TOP_INDEX(self):
        temp = None
        if(len(self.a)!= 0):
            temp = self.a[len(self.a) - 1]
        return temp

    def is_empty(self):
        boolTmep = False
        if(len(self.a) == 0):
            boolTmep = True
        return boolTmep

    def draw_stack(self):
        print(self.a)




def checkString(strng):
    stck = stack()
    for temp in strng:
        if temp == '<' or temp == '(' or temp == '[':
            stck.PUSH(temp)
        elif temp == '>':
            if stck.PEEK_TOP_INDEX() == '<':
                stck.POP()
        elif temp == ')':
            if stck.PEEK_TOP_INDEX() == '(':
                stck.POP()
        elif temp == ']':
            if stck.PEEK_TOP_INDEX() == '[':
                stck.POP()
        stck.draw_stack()
    return stck.is_empty()


print(checkString(string1))
print(checkString(string2))
print(checkString(string3))
print(checkString(string4))
print(checkString(string5))
