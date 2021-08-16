class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        super(Stack, self).__init__()

    def push(self, node):
        if self.is_empty():
            self.top = node
            self.top.next = None
            return
        temp = self.top
        self.top = node
        self.top.next = temp

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            temp = self.top
            if temp:
                self.top = temp.next
            temp.next =None
            print("popped item is : ",temp.data)

    def pick(self):
        print("There are not items in stack" if self.is_empty() else self.top.data)

    def is_empty(self):
        return True if self.top is None else False

    def traverse(self):
        if self.is_empty():
            print("stack is empty")
        top = self.top
        while top is not None:
            print("stack is element is : ", top.data)
            top = top.next


stack = Stack()

while True:
    action = int(input("Enter your choice."))
    if action == 1:
        stack.push(Node(input("Enter stack data ")))
    elif action == 2:
        stack.traverse()
    elif action == 3:
        stack.pick()
    elif action == 4:
        stack.pop()
    elif action == 5:
        break
