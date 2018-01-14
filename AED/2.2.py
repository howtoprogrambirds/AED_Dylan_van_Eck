class mystack(list):

    def push(self, value):
        self.append(value)

    def peek(self):
        return self[-1]

    def isEmpty(self):
        return self == []

s1 = mystack()
s1.push(4)
s1.push(5)
print(s1.isEmpty())
print(s1.peek())
s1.push(7)
print(s1.peek())
print(s1)
s1.pop()
print(s1)