from doubly_linkedlist import LinkedList

class Node(object):
    def __init__(self, data = None, next = None, prev = None):
        super(Node, self).__init__()
        self.data = data
        self.next = next
        self.prev = prev

class Queue(object):
    def __init__(self):
        self.queueLL = LinkedList()

    def push(self, data):
        return self.queueLL.push_back(data)

    def pop(self):
        return self.queueLL.pop_front()

    def top(self):
        return self.queueLL.top_front()

    def isEmpty(self):
        if self.queueLL.head is None:
            return True
        else:
            return False

    def size(self):
        return self.queueLL.size()