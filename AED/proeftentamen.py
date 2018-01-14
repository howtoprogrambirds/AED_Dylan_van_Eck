def identical_elements(a):
    for i in a:
        if i != a[0]:
            return False
    return True

b = [5,6,3,5,2];
c = [5,5,5,5,5];
print(identical_elements(b));
print(identical_elements(c));

def rec_identical_elements(a):
    if len(a) <= 1:
        return True;
    return a[0] == a[1] and rec_identical_elements(a[1:]);

d = [5,6,3,5,2];
e = [5,5,5,5,5];
print(rec_identical_elements(d));
print(rec_identical_elements(e));

class ListNode:
    def __init__(self,data,next_node):
        self.data = data;
        self.next = next_node;

def contains_None_data_node(n):
    if n == None:
        return False
    else:
        return n.data == None or contains_None_data_node(n.next)

n = ListNode(1,ListNode(2,ListNode(3,None)))
print(contains_None_data_node(n))
n = ListNode(1,ListNode(None,ListNode(3,None)))
print(contains_None_data_node(n))

class TreeNode:
    def __init__(self, data, left, right):
        self.data = data;
        self.left = left;
        self.right = right;

def count(n, x):
    if n == None:
        return 0;
    return (1 if (n.data == x) else 0) + count(n.left, x) + count(n.right, x)

n1 = TreeNode(1, None, None)
n2 = TreeNode(4, None, None)
n3 = TreeNode(3, None, None)
n4 = TreeNode(4, n1, None)
n5 = TreeNode(3, n2, None)
n6 = TreeNode(4, None, n3)
n7 = TreeNode(1, n4, n5)
n8 = TreeNode(5, None, n6)
n9 = TreeNode(4, n7, n8)
print(count(n9, 4))
print(count(n9, 3))

