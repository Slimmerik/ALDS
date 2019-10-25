import random
import string

class HashTableEntry:
    def __init__(self,strng):
        self.str = strng
        self.nextInChain = None

    def __repr__(self):
        return self.str

class SeparateChainingHashing:
    def __init__(self, length):
        self.len = length
        self.size = 0
        self.used = 0
        self.table = [None]*self.len
        print("len: " + str(self.len))

    def __repr__(self):
        s = '-----------------\n'
        return s

    def search(self,e):
        location = 0;
        for t in e.str:
            location = location + ord(t)
        tableLocation = location % self.len
        if self.table[tableLocation] != None:
            if self.table[tableLocation] == e:
                return e
            else:
                current = self.table[tableLocation]
                while current.nextInChain != None:
                    if current == e:
                        return current
                    else:
                        current = current.nextInChain
                if current == e:
                    return current
            return False
        return False

    def rehash(self, new_len):
        oldtable = self.table
        self.len = new_len
        self.table = [None]*self.len
        na = []

        for temp in oldtable:
            if temp != None:
                current = temp
                while current.nextInChain != None:
                    na.append(current)
                    current = current.nextInChain
                na.append(current)

        for t in na:
            t.nextInChain = None
        for p in na:
            self.insert(p)


    def insert(self,e):
        location = 0;
        for t in e.str:
            location = location + ord(t)
        tableLocation = location%self.len
        if self.table[tableLocation] == None:
            self.table[tableLocation] = e
        else:
            current = self.table[tableLocation]
            while current.nextInChain != None:
                current = current.nextInChain
            current.nextInChain = e
        if self.checkFullingGraad() > 0.75:
            self.rehash(self.len*2)
            print(self.table)


    def checkFullingGraad(self):
        aantalelementen = 0
        for t in self.table:
            if t is not None:
                current = t
                while current.nextInChain is not None:
                    aantalelementen += 1
                    current = current.nextInChain
                aantalelementen +=1
        re = aantalelementen / self.len
        return re


    def delete(self,e):
        location = 0;
        for t in e.str:
            location = location + ord(t)
        tableLocation = location % self.len
        if self.table[tableLocation] != None:
            if self.table[tableLocation] == e and self.table[tableLocation].nextInChain == None:
                self.table[tableLocation] = None
                return True
            else:
                current = self.table[tableLocation]
                last = None
                while current.nextInChain != None:
                    if current != e:
                        last = current
                        current = current.nextInChain
                    else:
                        if last == None:
                            self.table[tableLocation] = current.nextInChain
                            return True
                        else:
                            last.nextInChain = current.nextInChain
                            return True
                if current == e and last != None:
                    last.nextInChain = None
                    return True
                return False
        else:
            return False

if __name__ == '__main__':
    sch = SeparateChainingHashing(5)
    a1 = HashTableEntry("abc")
    a2 = HashTableEntry("abd")
    a3 = HashTableEntry("aae")
    a4 = HashTableEntry("abd")


    sch.insert(a1)
    print(sch.table)
    sch.insert(a2)
    print(sch.table)
    sch.insert(a3)
    print(sch.table)
    sch.insert(a4)
    print(sch.table)

    print("return correct obj: "  + str(sch.search(a4) == a4))
    print("obje a4 is not a2: "  + str(sch.search(a4) != a2))


    # print(sch.delete(a1))
    # print(sch.table)
    # print(sch.delete(a1))
    # print(sch.table)
    # print(sch.delete(a2))
    # print(sch.table)
    # print(sch.delete(a3))
    # print(sch.table)
    # print(sch.delete(a4))
    # print(sch.table)

    # print(sch.checkFullingGraaaaaaaad())
    # sch.rehash(5)


    print(sch.table)




def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

arraylength = 200
new_array  = []
for x in range(arraylength):
    new_array.append(HashTableEntry(randomString()))



for t in new_array:
    sch.insert(t)



for t in range(0,100):
    sch.delete(new_array[t])

