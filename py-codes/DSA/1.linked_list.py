class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def show(self):
        temp_node = self.head
        # print(self.head)
        while(temp_node):
            print(temp_node.data)
            temp_node = temp_node.next

ll = LinkedList()

ll.head = Node(1)
second = Node(2)
ll.head.next = second
third = Node(3)
second.next = third

ll.show()

