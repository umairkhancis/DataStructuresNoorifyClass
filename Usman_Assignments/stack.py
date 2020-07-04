class Node(object):
	def __init__(self, data = None, next = None, prev = None):
		super(Node, self).__init__()
		self.data = data
		self.next = next
		self.prev = prev

class Stack(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def push(self, data):
		new_node = Node(data)
		if self.tail is None:
			self.tail = new_node
			self.tail.next = None
			self.head = self.tail
			self.head.prev = None
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node
			new_node.next = None
		return True

	def pop(self):
		if self.head is None:
			raise ValueError("Empty Stack...")
			return
		elif self.tail == self.head:
			popped_data = self.tail.data
			self.head = None
			self.tail = self.head
		else:
			popped_data = self.tail.data
			self.tail = self.tail.prev
			self.tail.next = None
		return popped_data

	def top(self):
		if self.head is None:
			raise ValueError("Empty Stack...")
			return
		return self.tail.data

	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False

	def size(self):
		node = self.head
		count = 0
		while node:
			count += 1
			node = node.next

		return count