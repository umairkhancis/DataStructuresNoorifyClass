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
		if self.head is None:
			self.head = new_node
			return True
		
		node = self.head
		while node.next is not None: # if linkedlist is empty
			node = node.next

		node.next = new_node
		new_node.prev = node
		return True

	def pop_front(self):
		if self.head is None:
			raise ValueError("Nothing to pop...")
			return
		self.head.prev = None
		self.head = self.head.next

	def pop_back(self):
		if self.head is None:
			raise ValueError("Nothing to pop...")
			return
		
		node = self.head
		if node.next == None: # if first node is to be popped
			self.head = None
			return True

		while node.next is not None:
			node = node.next
            
		node.prev.next = None
		node.prev = None
		return True

	def top_front(self):
		if self.head is None:
			raise ValueError("Empty LinkedList...")
			return
		return self.head.data

	def top_back(self):
		if self.head is None:
			raise ValueError("Empty LinkedList...")
			return

		node = self.head	
		while node.next is not None:
			node = node.next
		return node.data

	def remove(self, data):
		if self.head is None:
			raise ValueError("Empty LinkedList...")
			return True

		if self.head.data == data: # if first node is to be removed
			self.head = self.head.next
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