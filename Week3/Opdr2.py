class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


class MyCircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        first = self.tail
        current = self.tail;
        if current != None:
            if current.next == None:
                s = s + str(current.data)
            else:
                current = current.next
                s = s + str(current.data)
                while current != first:
                    current = current.next
                    s = s + " -> "+ str(current.data)
        if not s:  # s == '':
            s = 'empty list'
        return s

    def append(self, e):
        if not self.tail:  # self.head == None:
            n = ListNode(e, None)
            self.tail = n
            return

        if self.tail.next == None:
            n2 = ListNode(e, self.tail)
            self.tail.next = n2
            self.tail = n2
            return

        if self.tail.next != None:
            n2 = ListNode(e, self.tail.next)
            self.tail.next = n2
            self.tail = n2
            return

    def delete(self, e):

        if not self.tail:
            return
        if self.tail.next == None:
            if self.tail.data == e:
                seld.tail = None
                return
            return
        if self.tail.next != None:
            current = self.tail
            if current.next.data == e:
               current.next = current.next.next
            current = current.next
            while self.tail != current:
                if current.next.data == e:
                    current.next = current.next.next
                current = current.next




if __name__ == '__main__':
    mylist = MyCircularLinkedList()
    print(mylist)
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    mylist.append("koe")
    mylist.append("foo")
    mylist.append("bar")
    print(mylist)
    mylist.delete(2)
    print(mylist)
    mylist.delete(1)
    print(mylist)
    mylist.delete(3)
    print(mylist)
    mylist.append("7")
    print(mylist)
    mylist.delete("foo")
    print(mylist)