class Node(object):
    def __init__(self, data, next=None, prev=None):
        super(Node, self).__init__()
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return "{} -> {}".format(self.data, self.next,self.prev)


class Stack(object):
    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None
        self.tail = None


    def _get_new_node(self, data):
        node = Node(data)
        node.data = data
        node.next = None
        node.prev = None
        return node


    def push(self, data):
        new_node = self._get_new_node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.previous = None
            self.tail.next = None
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        return True


    def pop(self):
        if not self.head:
            raise ValueError("Empty list ")
        elif self.head is not self.tail:
            self.head = self.head.next
            self.head.prev = None
            return
        else:
            self.head = self.tail = None
            return

    def top(self):
        if not self.head:
            raise ValueError("Empty list ")
        return self.head

    def isEmpty(self):
        if self.head:
            return True
        return False


    def size(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count
