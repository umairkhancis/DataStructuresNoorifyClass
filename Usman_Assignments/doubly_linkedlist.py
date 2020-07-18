class Node(object):
	def __init__(self, data = None, next = None, prev = None):
		super(Node, self).__init__()
		self.data = data
		self.next = next
		self.prev = prev


	def __str__(self):
		return "{} -> {}".format(self.data, self.next)

class LinkedList(object):
	def __init__(self):
		super(LinkedList, self).__init__()
		self.head = None
		self.tail = None

	def size(self):
		node = self.head
		count = 0
		while node:
			count += 1
			node = node.next
		return count

	def find(self, data):
		node = self.head
		found = False

		while node and found is False:
			if node.data == data:
				found = True
			else:
				node = node.next

		if node is None:
			raise ValueError("Could not found...")
		return node

	def update(self, data, new_data):
		node = self.head
		updated = False
		while node and updated is False:
			if node.data == data:
				node.data = new_data
				updated = True
			else:
				node = node.next
		if node is None:
			raise ValueError("Could not found...")
		return updated

	def push_front(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return True
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
			return True

	def push_back(self, data):
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

	def pop_front(self):
		if self.head is None:
			raise ValueError("Nothing to pop...")
			return
		popped_data = self.head.data
		self.head.prev = None
		self.head = self.head.next
		return popped_data

	def pop_back(self):
		popped_data = None
		if self.tail is None:
			raise ValueError("Nothing to pop...")
			return
		elif self.head == self.tail:
			popped_data = self.head.data
			self.head = None
			self.tail = self.head
		else:
			popped_data = self.tail.data
			self.tail = self.tail.prev
			self.tail.next = None
		return popped_data

	def top_front(self):
		if self.head is None:
			raise ValueError("Empty LinkedList...")
			return
		return self.head.data

	def top_back(self):
		if self.head is None:
			raise ValueError("Empty LinkedList...")
			return
		return self.tail.data

	def remove(self, data):
		if self.head is None:
			raise ValueError("Empty LinkedList...")
			return True

		if self.head.data == data: # if first node is to be removed
			self.head.prev = None
			self.head = self.head.next
			return True

		if self.tail.data == data: # if last node is to be removed
			self.tail = self.tail.prev
			self.tail.next = None
			return True

		node = self.head
		while node is not None:
			if node.data == data:
				node.prev.next = node.next
				node.prev = None
				node.next =None
				return True
			node = node.next

		if node is None:
			raise ValueError("Node not found...")

	def reverse(self, method = "iterative"):
		if method == "iterative":
			return self._reverse_iterative()
		else:
			self._reverse_recurrsive(self.head)
			return self.head

	def _reverse_iterative(self):
		temp = None
		curr_node = self.head

		while curr_node is not None:
			temp = curr_node.prev
			curr_node.prev = curr_node.next
			curr_node.next = temp
			curr_node = curr_node.prev

		if temp is not None:
			self.head = temp.prev

	def __str__(self):
		result = "\n*** LinkedList ***\n"
		node = self.head
		while node:
			result += "{} -> ".format(node)
			node = node.next
		result += "None"

		return result