class Node(object):
	def __init__(self, data = None, next = None):
		super(Node, self).__init__()
		self.data = data
		self.next = next

	def __str__(self):
		return "{} -> {}".format(self.data, self.next)

class LinkedList(object):
	def __init__(self):
		super(LinkedList, self).__init__()
		self.head = None

	def size(self):
		# print("Complete the implementation")
		node = self.head
		count = 0
		while node:
			count += 1
			node = node.next
		return count

	def find(self, data):
		# print("Complete the implementation")
		if self.head is None:
			raise ValueError("Nothing to find...")
		

		node = self.head
		while node is not None:
			if node.data == data:
				return True
			node = node.next
		raise ValueError("Node not found...")

	def update(self, data, new_data):
		# print("Complete the implementation")
		node = self.head
		while node is not None:
			if node.data == data:
				node.data = new_data
				return True
			else:
				raise ValueError("Node not found...")
			node = node.next
		if self.head is None:
			raise ValueError("Node not found...")

	def push_front(self, data):
		# print("Complete the implementation")
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		return True

	def pop_front(self):
		# print("Complete the implementation")
		if self.head is None:
			raise ValueError("Nothing to pop...")
		self.head = self.head.next
		return True

	def top_front(self):
		# print("Complete the implementation")
		if self.head is None:
			raise ValueError("Nothing to find...")
		return self.head.data

	def push_back(self, data):
		# print("Complete the implementation")
		new_node = Node(data)
		
		if self.head is None:
			self.head = new_node
			return True
		
		node = self.head
		while node.next is not None:
			node = node.next
		node.next = new_node
		return True

	def pop_back(self):
		# print("Complete the implementation")
		if self.head is None:
			raise ValueError("Nothing to pop...")
			return
		node = self.head

		if node.next is None:
			self.head = None
			return True

		while node.next.next is not None:
			node = node.next
		node.next = None
		return True

	def top_back(self):
		# print("Complete the implementation")
		if self.head is None:
			raise ValueError("Nothing to pop...")
			return

		node = self.head

		while node.next is not None:
			node = node.next
		return node.data

	def remove(self, data):
		# print("Complete the implementation")

		node = self.head
		# if first node is to be deleted
		if node is not None:
			if node.data == data:
				self.head = node.next
				return True

		while node is not None:
			if node.data == data:
				break
			prev_node = node
			node = node.next

		if node is None:
			raise ValueError("Node not found...")
			return False

		# Unlink that node
		prev_node.next = node.next
		return True

	def _reverse_iterative(self):
		# print("Complete the implementation")
		if self.head is None:
			return False

		prev_node = None
		this_node = self.head
		while node is not None:
			next_node = this_node.next
			this_node.next = prev_node
			prev_node = this_node
			this_node = next_node
		self.head = prev_node

	def reverse(self, method = "iterative"):
		if method == "iterative":
			return self._reverse_iterative()
		else:
			self._reverse_recurrsive (self.head)
			return self.head
	
	def _reverse_recurrsive(self, curr_node):
		# print("Complete the implementation")
		if curr_node is None:
			return curr_node

		if curr_node.next is None:
			return curr_node

		reverse_node = _reverse_recurrsive(curr_node.next)
		curr_node.next.next = reverse_node
		curr_node.next = None
		return reverse_node
	
	def __str__(self):
		result = "\n*** LinkedList ***\n"
		node = self.head
		while node:
			result += "{} -> ".format(node)
			node = node.next

		result += "None"

		return result