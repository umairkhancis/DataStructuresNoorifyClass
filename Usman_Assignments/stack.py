class Node(object):
	def __init__(self, data = None, next = None, prev = None):
		super(Node, self).__init__()
		self.data = data
		self.next = next
		self.prev = prev

class Stack(object):
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return True

		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node
		return True

	def pop(self):
		if self.head is None:
			raise ValueError("Empty Stack...")
			return
		
		popped_data = self.head.data
		self.head.prev = None
		self.head = self.head.next
		return popped_data

	def top(self):
		if self.head is None:
			raise ValueError("Empty Stack...")
			return
		return self.head.data

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