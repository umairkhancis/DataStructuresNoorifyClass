from doubly_linkedlist import LinkedList
class Queue(LinkedList):
    def __init__(self):
        super(Queue, self).__init__()
        self.head = None
        self.tail = None


    def push(self, data):
        push2 = LinkedList.push_front(self, data)
        return push2

    def pop(self):
        pop2 = LinkedList.pop_back(self)
        return pop2

    def top(self):
        top2 = LinkedList.top_back(self)
        return top2

    def isEmpty(self):
        if self.head:
            return False
        return True

    def size(self):
        size2 = LinkedList.size(self)
        return size2
