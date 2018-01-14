class mystack(list):
    def push(self, value):
        self.append(value)

    def peek(self):
        if(len(self) > 0):
            return self[len(self)-1]
        else:
            return 0

    def isEmpty(self):
        return self == []

def isValid(a):
    print("left elements: ", a)
    if(a == []):
        print("this stack is: valid")
    else:
        print("this stack is: invalid")

def bracketstack(st):
    for i in range (0, len(s1)):
        print("s1: " + s1[i])
        if(st.peek() == '('):
            if(s1[i] == ']' or s1[i] == '>'):
                break
            elif(s1[i] == ")"):
                st.pop()
            else:
                st.push(s1[i])
        elif(st.peek() == '['):
            if (s1[i] == ')' or s1[i] == '>'):
                break
            elif (s1[i] == "]"):
                st.pop()
            else:
                st.push(s1[i])
        elif (st.peek() == '<'):
            if (s1[i] == ')' or s1[i] == '}'):
                break
            elif (s1[i] == ">"):
                st.pop()
            else:
                st.push(s1[i])
        else:
            st.push(s1[i])

    isValid(st)

s1 = "())"
str = mystack()

bracketstack(str)


