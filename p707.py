class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        assert isinstance(node, Node)
        self.next = node


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.count = 0
        self.tail = None

    def __str__(self):
        node = self.head
        l = []
        while node is not None:
            l.append(node.val)
            node = node.next
        return str(l)

    def _get_node(self, index: int) -> Node:
        if index > self.count - 1:
            return None
        if index < 0:
            return None

        node = self.head
        i = 0
        while i < index:
            node = node.next
            i += 1
        return node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get_node(index)
        return node.val if node is not None else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            new_head = Node(val)
            new_head.set_next(self.head)
            self.head = new_head
        self.count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.tail is None:
            self.tail = Node(val)
            self.head = self.tail
        else:
            new_tail = Node(val)
            self.tail.set_next(new_tail)
            self.tail = new_tail
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of
        linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.count:
            return
        if index == 0:
            return self.addAtHead(val)
        if index == self.count:
            return self.addAtTail(val)

        # find node before index-th node
        node = self._get_node(index - 1)

        # insert new node
        next_node = node.next
        new_node = Node(val)
        node.next = new_node
        new_node.next = next_node

        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.count - 1:
            return

        # delete at head
        elif index == 0:
            self.head = self.head.next
        # delete at tail
        elif index == self.count - 1:
            self.tail = self._get_node(index - 1)
            self.tail.next = None
        else:
            node = self._get_node(index - 1)
            node.next = node.next.next
        self.count -= 1


if __name__ == '__main__':
    obj = MyLinkedList()
    command = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    val = [[], [1], [3], [1, 2], [1], [1], [1]]

    command = ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead",
               "addAtTail",
               "get", "addAtHead", "addAtIndex", "addAtHead"]
    val = [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]

    for i, c in enumerate(command):
        if c == "addAtHead":
            obj.addAtHead(val[i][0])
        elif c == 'addAtTail':
            obj.addAtTail(val[i][0])
        elif c == 'addAtIndex':
            obj.addAtIndex(val[i][0], val[i][1])
        elif c == 'get':
            print(obj.get(val[i][0]))
        elif c == 'deleteAtIndex':
            obj.deleteAtIndex(val[i][0])

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
