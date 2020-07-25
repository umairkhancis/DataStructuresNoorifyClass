from doubly_linkedlist import LinkedList
class Stack(LinkedList):
    def __init__(self):
        super(Stack, self).__init__()
        self.head = None


    def push(self, data):
        push1=LinkedList.push_front(self,data)
        return push1

    def pop(self):
        pop1=LinkedList.pop_front(self)
        return pop1


    def top(self):
        top1=LinkedList.top_front(self)
        return top1

    def isEmpty(self):
        if self.head:
            return False
        return True

    def size(self):
        size1=LinkedList.size(self)
        return size1
