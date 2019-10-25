class worddict():
    def __init__(self):
        self.dict = {}


    def __repr__(self, nspaces=0):
        string= ""
        for x, y in self.dict.items():
           string = string + str(x) + " " + str(y) + "\n";
        return string

    def insert(self, word):
        if self.dict.get(word) is None:
            self.dict[word] = 1
        else:
            self.dict[word] = self.dict[word] + 1

    def readFile(self, file):
        a = open(file, 'r')
        b = a.read().split(" ")
        for first in b:
            b = first.split("\n")
            for second in b:
                if second is not "\n" and second is not "":
                    self.insert(second)


    def writeFile(self, name):
        a = open(name, 'w')
        a.write(str(self))


a = worddict()
print("--------Methode 1")
# a.insert("a")
# a.insert("a")
# a.insert("b")
# a.insert("c")
# a.insert("a")
a.readFile("words.txt")
a.writeFile("dict.txt")
print(a)

print ("-------------Methode 2")
class Node():
    def __init__(self, val):
        self.children = []
        self.value = val
        self.number = None

    def __repr__(self):
        print("tree")

    def makeTree(self, dict):
        addingletters = ""
        currentNode = None
        for key in dict.dict:
            if currentNode is not None:
                currentNode.number = dict.dict[addingletters]
            length = len(key)
            addingletters = ""
            currentNode = self
            for letter in key:
                addingletters = addingletters + letter
                nodepressend = False

                for temp in currentNode.children:
                    if temp.value == addingletters:
                        nodepressend = True
                        currentNode = temp
                if nodepressend is False:
                    tempNode = Node(addingletters)
                    currentNode.children.append(tempNode)
                    currentNode = tempNode


class dicttree():
    def __init__(self ):
        self.root = Node(None)

    def makeTree(self,di):
        if self.root:
            self.root.makeTree(di)
        else:
            None

tree = dicttree()
tree.makeTree(a)
print("zie opdrcht 3")
print("end")



