import json

class Node(object):
	def __init__(self, data = None, next = None):
		super(Node, self).__init__()
		self.data = data
		self.next = next

	def __str__(self):
		return "{} -> {}".format(self.data, self.next)

class LinkedList(object):
	def __init__(self, head = None):
		super(LinkedList, self).__init__()
		self.head = head

	def size(self):
		count = 0
		current_node = self.head
		while current_node:
			count += 1
			current_node = current_node.next

		return count

	def find(self, data):
		current_node = self.head
		while current_node:
			if current_node.data == data:
				return Node(current_node.data, current_node.next)
			current_node = current_node.next

		return None

	def update(self, data, new_data):
		current_node = self.head
		while current_node:
			if current_node.data == data:
				current_node.data = new_data
				return True
			current_node = current_node.next

		return False

	def append(self, data):
		new_node = self.__get_new_node__(data)

		if self.head:
			last_node = self.__get_last_node__()
			last_node.next = new_node
		else:
			self.head = new_node
			return True

	def insert(self, data):
		new_node = self.__get_new_node__(data)

		if self.head:
			last_node = self.__get_last_node__()
			last_node.next = new_node
		else:
			self.head = new_node
			return True

	def remove(self, data):
		current = self.head
		prev = self.head
		while current:
			if current.data == data:
				if current == self.head:
					self.head = current.next
				prev.next = current.next
				current = None
				return True

			prev = current
			current = current.next

		return False

	def _reverse_iterative(self):
		current = self.head
		prev = None
		while current:
			temp_node = current.next
			current.next = prev
			prev = current
			current = temp_node

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
			return
		self._reverse_recurrsive(curr, curr.next)
		curr.next = prev

	def __get_new_node__(self, data):
		node = Node()
		node.data = data
		node.next = None

		return node

	def __get_last_node__(self):
		last_node = self.head
		while last_node and last_node.next:
			last_node = last_node.next

		return last_node
	
	def __str__(self):
		result = "\n*** LinkedList ***\n"
		node = self.head
		while node:
			result += "{} -> ".format(node)
			node = node.next

		result += "None"

		return result






