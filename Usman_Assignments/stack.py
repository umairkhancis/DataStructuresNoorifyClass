from doubly_linkedlist import LinkedList

class Node(object):
	def __init__(self, data = None, next = None, prev = None):
		super(Node, self).__init__()
		self.data = data
		self.next = next
		self.prev = prev

class Stack(object):
	def __init__(self):
		self.stackLL = LinkedList()

	def push(self, data):
		return self.stackLL.push_back(data)

	def pop(self):
		return self.stackLL.pop_back()

	def top(self):
		return self.stackLL.top_back()

	def isEmpty(self):
		if self.stackLL.head is None:
			return True
		else:
			return False

	def size(self):
		return self.stackLL.size()