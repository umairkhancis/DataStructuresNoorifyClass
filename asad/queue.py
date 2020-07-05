class Node(object):

	def __init__(self, data = None, next = None, prev = None):
		super(Node, self).__init__()
		self.data = data
		self.next = next
		self.prev = prev

class Queue(object):
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		node = self.head
		while node.next is not None:
			node = node.next
		node.next = new_node
		new_node.prev = node
		return True	 	

	def pop(self):
		if self.head is None:
			raise ValueError("nothing to pop")
			return
		poped_data = self.head.data		
		self.head.prev = None		
		self.head = self.head.next
		return poped_data

	def top(self):
		if self.head is None:
			raise ValueError("stack is empty")
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
			count+=1
			node = node.next
		return count