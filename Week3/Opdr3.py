class BSTNode:
    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self, nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' ' * nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def rinsert(self, e):
        if e == self.element:
            return False

        if e > self.element and self.right == None:
            self.right = BSTNode(e, None, None)
            return True
        elif e < self.element and self.left == None:
            self.left = BSTNode(e, None, None)
            return True

        if e > self.element:
            return self.right.rinsert(e)
        else:
            return self.left.rinsert(e)




    def insert(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True;

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e, None, None)
            else:
                parent.left = BSTNode(e, None, None)
        return not found

    def insertArray(self, a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a) - 1
        mid = (low + high + 1) // 2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a, low, mid - 1)
        if high > mid:
            self.insertArray(a, mid + 1, high)

    def rsearch(self, e):
        if str(self.element) == str(e):
            return self
        else:
            if self.right != None:
                self.right.rsearch(e)
            if self.left != None:
                self.left.rsearch(e)




    def search(self, e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def search2(self, e):
        if self.element == e:
            return self
        parent = self.getParent(e)
        if parent == None:
            return None
        if parent.element < e:
            return parent.right
        return parent.left

    def getParent(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left;
        else:
            return None

        while not found and current:
            if current.element == e:
                found = True
            else:
                parent = current
                if current.element < e:
                    current = current.right
                else:
                    current = current.left
        if found:
            return parent
        else:
            return None

    def parentMinRightTree(self):
        parent = self.right
        current = parent.left
        while current.left:
            parent = current
            current = current.left
        return parent

    def delete(self, e):
        parent = self.getParent(e);

        if parent == None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left == None:
                parent.right = parent.right.right
                return True
            else:
                if current.right == None:
                    parent.right = parent.right.left
                    return True
        else:
            current = parent.left
            if current.left == None:
                parent.left = parent.left.right
                return True
            else:
                if current.right == None:
                    parent.left = parent.left.left
                    return True
        if current.right.left == None:
            current.element = current.right.element
            current.right = current.right.right
            return True
        node = current.parentMinRightTree()
        current.element = node.left.element
        node.left = node.left.right
        return True
    def max(self):
        max = None
        if self.right == None:
            return self.element
        else:
            return self.right.max();

    def showLevelOrder(self, levelorder, level):
        if len(levelorder) is level:
            levelorder.append([self.element])
        else:
            levelorder[level].append(self.element)

        if self.left != None:
            self.left.showLevelOrder(levelorder,level+1)
        if self.right != None:
            self.right.showLevelOrder(levelorder,level+1)
        if self.right and self.left is None:
            return True


class BST:
    def __init__(self, a=None):
        if a:
            mid = len(a) // 2
            self.root = BSTNode(a[mid], None, None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid + 1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def search(self, e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def rsearch(self, e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def showLevelOrder(self):
        a = []
        if self.root:
            self.root.showLevelOrder(a, 0)
            b = []
            for temp in a:
                for temp2 in temp:
                    b.append(temp2)
            return b

        else:
            return None

    def max(self):
        if self.root:
            return self.root.max()

    def insert(self, e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BSTNode(e, None, None)
                return True
        else:
            return False

    def rinsert(self, e):
        if e:
            if self.root:
                return self.root.rinsert(e)
            else:
                self.root = BSTNode(e, None, None)
                return True
        else:
            return False


    def delete(self, e):
        if self.root and e:
            if self.root.element == e:
                if self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None:
                    self.root = self.root.left
                elif self.root.right.left == None:
                    self.root.element = self.root.right.element
                    self.root.right = self.root.right.right
                else:
                    node = self.root.parentMinRightTree();
                    self.root.element = node.left.element
                    node.left = node.left.right
                return True
            else:
                return self.root.delete(e)
        else:
            return False


if __name__ == '__main__':

    b = BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    #b = BST([6])
    print(b)
    # node = b.search(3)
    # if node != None:
    #     print(node.element)
    #
    print(b.insert(18))
    print(b.insert(16))
    print(b.insert(17))
    #
    print(b)
    # print(b.max())
    # print(b.insert(19))
    # print(b.max())
    #
    # print("--------rsearch")
    # print(b.rsearch(19))
    # print(b.rsearch(20))
    # print(b.rsearch(1))

    print("--------rinsert")
    print(b.rinsert(25))
    print(b.rinsert(25))
    print(b.rinsert(2))
    print(b)

    print("--------showorder")
    a = b.showLevelOrder()
    print(a)