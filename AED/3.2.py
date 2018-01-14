class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail
        if current != None:
            s = s + str(current.next)
            current = current.next.next
            while current != self.tail.next:
                s = s + " -> " + str(current)
                current = current.next
        if not s: # s == '':
            s = 'empty list'

        return s

    def addLast(self,e):
        if not self.tail: # self.tail == None:
            self.tail = ListNode(e,None)
            self.tail.next = self.tail
        else:
             self.tail.next = ListNode(e, self.tail.next)
             self.tail = self.tail.next

    def delete(self,e):
        if self.tail: # self.tail!= None:
            if self.tail.data == e:
                if self.tail == self.tail.next:
                    self.tail = None
                else:
                    current = self.tail
                    while current.next != self.tail:
                        current = current.next
                    current.next = current.next.next
                    self.tail = current
            elif self.tail.next != self.tail:
                current = self.tail
                while current.next.data != e and current.next != self.tail:
                    current = current.next
                if current.next.data == e:
                    current.next = current.next.next

if __name__ == '__main__':
    mylist =  MyLinkedList()
    print(mylist)
    mylist.addLast(1)
    # print(mylist)
    mylist.addLast(2)
    mylist.addLast(3)
    print(mylist)
    mylist.delete(1)
    print(mylist)
    mylist.delete(1)
    print(mylist)
    mylist.delete(3)
    print(mylist)
