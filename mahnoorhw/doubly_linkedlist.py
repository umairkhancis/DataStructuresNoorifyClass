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
        node = Node(data)
        node.data = data
        node.next = None
        node.prev = None
        return node


    def find(self, data):
        curr_node = self.head

        while curr_node:
            if curr_node.data == data:
                return Node(curr_node.data,curr_node.next)
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
            self.head = self.tail = new_node
            self.head.previous = None
            self.tail.next = None
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        return True

    def pop_front(self):

        if not self.head:
            raise ValueError("Empty list ")
        elif self.head is not self.tail:
            prev_head = self.head
            self.head = prev_head.next
            return prev_head.data
        else:
            prev_head = self.head
            self.head = self.tail = None
            return prev_head.data



    def top_front(self):
        if not self.head:
            raise ValueError("Empty list ")
        return self.head.data

    def push_back(self, data):
        new_node = self._get_new_node(data)

        if self.tail is None:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None

        return True



    def pop_back(self):
        if self.head is None:
            raise ValueError("Empty list ")
        elif self.head is not self.tail:
            prev_tail = self.tail
            self.tail = prev_tail.prev
            return prev_tail.data

        else:
            prev_tail = self.tail
            self.head = self.tail = None
            return prev_tail.data


    def top_back(self):
        if not self.tail:
            raise ValueError("Empty list ")
        return self.tail.data

    def remove(self, data):
        curr = self.head

        while curr:
            if curr.data == data and curr == self.head:
                if not curr.next:
                    curr = None
                    self.head = self.tail = None
                else:
                    next= curr.next
                    curr.next = None
                    curr.prev = None
                    self.head = next
                    self.head.prev = None
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
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

                return True
            else:
                curr = curr.next
        raise ValueError("Empty list ") # data not found


    def _reverse_iterative(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if prev:
            self.head = prev
        return self.head


    def reverse(self, method="recurrsive"):
        if method == "iterative":
            return self._reverse_iterative()
        else:
            self._reverse_recurrsive(None, self.head)
            return self.head

    def _reverse_recurrsive(self, prev, curr):

        if not curr:
            self.head = prev
            return
        self._reverse_recurrsive(curr, curr.next)
        curr.next = prev

    def __str__(self):
        result = "\n*** LinkedList ***\n"
        node = self.head
        while node:
            result += "{} -> ".format(node)
            node = node.next

        result += "None"

        return result