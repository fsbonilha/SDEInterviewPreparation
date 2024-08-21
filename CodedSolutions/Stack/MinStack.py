class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MinStack:

    def __init__(self):
        self.currMin = None
        self.head = None

    def push(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        if not self.currMin or val <= self.currMin.val:
            newMin = Node(val)
            newMin.next = self.currMin
            self.currMin = newMin

    def pop(self) -> None:
        val = self.head.val
        self.head = self.head.next
        if val == self.currMin.val:
            self.currMin = self.currMin.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.currMin.val
