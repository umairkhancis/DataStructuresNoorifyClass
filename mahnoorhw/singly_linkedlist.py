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

	def _get_new_node(self, data):
		node = Node()
		node.data = data
		node.next = None
		return node


	def size(self):
		count = 0
		current_node = self.head
		while current_node:
			count += 1
			current_node = current_node.next
		return count

	def _get_last_node(self):
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		return last_node

	def find(self, data):
		curr_node = self.head
		while curr_node:
			if curr_node.data == data:
				return Node(curr_node.data, curr_node.next)
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
		prev_node = self.head
		self.head = new_node
		new_node.next = prev_node

		return True


	def pop_front(self):
		if not self.head:
			raise ValueError("Empty list ")
		prev_node = self.head
		self.head = prev_node.next

	def top_front(self):
		if not self.head:
			raise ValueError("Empty list ")
		return self.head

	def push_back(self, data):
		new_node = self._get_new_node(data)
		if self.head:
			last_node = self._get_last_node()
			last_node.next = new_node
		else:
			self.head = new_node
		return True

	def pop_back(self):
		if not self.head:
			raise ValueError("Empty list ")
		prev = None
		curr =self.head
		while curr.next:
			prev = curr
			curr = curr.next
		if not prev:
				self.head = None
		else:
			prev.next = None
			curr = None

	def top_back(self):
		if not self.head:
			raise ValueError("Empty list ")
		else:
			prev = None
			curr = self.head
			while curr.next:
				prev = curr
				curr = curr.next
			if not prev:
				return self.head
			else:
				return curr


	def remove(self, data):
		curr = self.head
		while curr:
			#case 1
			if curr.data == data and curr == self.head:
				if not curr.next:
					self.head= None
					curr = None
					return True
				#case 2
				else:
					next = curr.next
					curr = None
					self.head = next
					return True
			elif curr.data == data:
				if curr.next:
					next = curr.next
					prev.next = next
					curr = None
					return True
				else:
					prev.next = None
					curr = None
					return True
			else:
				prev = curr
				curr = curr.next
		raise ValueError("Empty list ")



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

	def reverse(self, method = "recurrsive"):
		if method == "iterative":
			return self._reverse_iterative()
		else:
			self._reverse_recurrsive(None, self.head)
			return self.head


	def _reverse_recurrsive(self, prev, curr):
		if not curr:
				self.head = prev
				return self.head
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