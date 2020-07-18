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
		self._size = 0

	def update(self, udata, new_data):
		node = self.head
		updated = False
		while node and updated is False:
			if node.data == udata:
				node.data = new_data
				updated = True
			else:	
				node = node.next
		if node is None:
			raise ValueError("data not found")	
		return updated	

	def size(self):
		return self._size

	def find(self,fdata):
		node = self.head
		if  self.head is None:  # if linked list is empty
			raise ValueError("linkedlist is empty")
			return True
		
		if self.head.data == fdata: # if data to be search is at start
			return node
		
		if self.tail.data == fdata: # if data to be search is at end
			return node

		found = False
		while node and found is False:
			if node.data == fdata:
				found = True
			else:	
				node = node.next
		if node is None: # if data to be search is not in linkedlist
			raise ValueError("data not found") 
		return node

	def push_front(self, data): #insert at the start of linked list
		new_node = Node(data)
		self._size += 1 
		if self.head is None:
			self.head = new_node
			return True
		new_node.next = self.head	
		self.head.prev = new_node
		self.head = new_node
		return True	

	def push_back(self, data): #insert at the end of linked list
		new_node = Node(data)
		self._size += 1
		if self.head is None: # if linked list is empty
			self.head = new_node
			self.tail = new_node
			return True
		node = self.tail 
		node.next = new_node
		new_node.prev = node
		self.tail = new_node
		return True
			
	def pop_back(self):
		if self.tail is None:
			raise ValueError("nothing to pop")
			return
		self._size -= 1
		if self.head.next == None:
			self.head = None
			self.tail = None
			return True
		node = self.tail
		self.tail = node.prev
		node.prev.next = None
		node.prev = None
		return True	

	def pop_front(self):
		if self.head is None:
			raise ValueError("nothing to pop")
			return
		self._size -= 1	
		poped_data = self.head.data
		self.head.prev = None	
		self.head = self.head.next
		return poped_data

	def top_back(self):
		if self.head is None:
			raise ValueError("nothing to pop")
			return
		node = self.tail	
		return node.data

	def top_front(self):
		if self.head is None:
			raise ValueError("nothing to pop")
			return
		return self.head.data

	def remove(self, data):
		if  self.head is None:  # if linked list is empty
			raise ValueError("nothing to remove")
			return True
		
		if self.head.data == data: # if data to be removed is at start
			self.head = self.head.next
			self._size -= 1
			return True
		
		if self.tail.data == data: # if data to be removed is at end
			self.tail = self.tail.prev
			self.tail.next = None
			self._size -= 1
			return True	
			
		node = self.head
		while node is not None:
			if node.data == data:
				self._size -= 1
				node.prev.next = node.next
				node.prev = None
				node.next =None
				return True
			node = node.next

		if node is None: # if data to be removed is not in the linkedlist
			raise ValueError("item not in linkedlist")			


	def _reverse_iterative(self):
		temp = None
		current = self.head   
		while current is not None: 
			temp = current.prev  
			current.prev = current.next
			current.next = temp 
			current = current.prev 
		if temp is not None: 
			self.head = temp.prev 

	def _reverse_recurrsive(self, prev,curr):
		if not curr:
			self.head = prev
			return self.head 
		self._reverse_recurrsive(curr,curr.next)
		curr.next = prev
	
	def reverse(self, method = "iterative"):
		if method == "iterative":
			return self._reverse_iterative()
		else:
			self._reverse_recurrsive(self.head.prev,self.head)
			return self.head
	
	def __str__(self):
		result = "\n*** LinkedList ***\n"
		node = self.head
		while node:
			result += "{} -> ".format(node)
			node = node.next
		result += "None"

		return result 

