class Node(object):
    def __init__(self, data, next=None, prev=None):
        super(Node, self).__init__()
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return "{} -> {}".format(self.data, self.next,self.prev)


class LinkedList(object):
    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None
        self.tail = None


    def size(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count +=1
            curr_node = curr_node.next
        return count

    def _get_new_node(self, data):
        node = Node()
        node.data = data
        node.next = None
        node.prev = None
        return node


    def find(self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return Node(curr_node.data,curr_node.next,curr_node.pev)
            curr_node = curr_node.next
        raise ValueError("value not found")

    def update(self, data, new_data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                curr_node.data = new_data
                return True
            curr_node = curr_node.next
        raise ValueError("value not found")

    def push_front(self, data):
        new_node = self._get_new_node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node

    def pop_front(self):

        if not self.head:
            raise ValueError("Empty list ")
        else:
            curr = self.head
            self.head = curr.next
            self.head.prev = None
            curr = None



    def top_front(self):
        if not self.head:
            raise ValueError("Empty list ")
        return self.head


    def push_back(self, data):

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None

        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail = new_node
        return True


    def pop_back(self):
        if self.tail is None:
            raise  ValueError("Empty list ")
        else:
            curr = self.tail
            self.tail = curr.prev
            self.tail.next = None
            curr = None
        return True



    def top_back(self):
        if not self.tail:
            raise ValueError("Empty list ")
        return self.tail

    def remove(self, data):
        curr = self.head

        while curr:
            if curr.data == data and curr == self.head:
                if not curr.next:
                    curr = None
                    self.head = None
                else:
                    next= curr.next
                    curr.next = None
                    curr.prev = None
                    self.head = next
                    curr = None     
                return True  # data removed
            elif curr.data == data:
                if curr.next:
                    next = curr.next
                    prev = curr.prev
                    prev.next = next
                    next.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                return True
            else:
                curr = curr.next
        return False  # data not found


    def _reverse_iterative(self):
        if self.head is None:
            raise  ValueError("Empty list ")
        else:
            curr_node = self.head
            prev_node = None
            while curr_node:
                next = curr_node.next
                curr_node.next = prev_node
                curr_node.prev = next
                prev_node = curr_node
                curr_node = curr_node.prev
        self.head = prev_node
        return True

    def reverse(self, method="recurrsive"):
        if method == "iterative":
            return self._reverse_iterative()
        else:
            self._reverse_recurrsive(None, self.head)
            return self.head

    def _reverse_recurrsive(self, prev, curr):

        if curr.next is None:
            # swap next and prev pointers for the current node
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev

            # update head
            self.head = curr
            return self.head

            # swap next and prev pointers for the current node
        prev = curr.prev
        curr.prev = curr.next
        curr.next = prev

        # recur with the next node
        self.head = _reverse_recurrsive(self.head, curr.prev)
        return self.head

        #print("Complete the implementation")

    def __str__(self):
        result = "\n*** LinkedList ***\n"
        node = self.head
        while node:
            result += "{} -> ".format(node)
            node = node.next

        result += "None"

        return result