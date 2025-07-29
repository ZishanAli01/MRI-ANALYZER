class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if not current:
            return

        if previous:
            previous.next = current.next
        else:
            self.head = current.next

    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements