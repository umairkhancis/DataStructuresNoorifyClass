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
		node = self.head
		count = 0
		while node:
			count+=1
			node = node.next
		return count

	def find(self,fdata):
		node = self.head
		found = False
		while node and found is False:
			if node.data == fdata:
				found = True
			else:	
				node = node.next
		if node is None:
			raise ValueError("data not found")
		return node

	def push_front(self, data): #insert at the start of linked list
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return True
		else:	
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
			return True

	def push_back(self, data): #insert at the end of linked list
		new_node = Node(data)
		if self.head is None: # if linked list is empty
			self.head = new_node
			return True
		node = self.head #otherwise if it contain some nodes then traverse through at the end of list and set next of the last node to new_node
		while node.next is not None:
			node = node.next
		node.next = new_node
		new_node.prev = node
		return True
			
	def pop_back(self):
		if self.head is None:
			raise ValueError("nothing to pop")
			return
		
		node = self.head
		
		if node.next == None:
			self.head = None
			return True

		while node.next is not None:
			node = node.next
		node.prev.next = None
		node.prev = None
		return True	

	def pop_front(self):
		if self.head is None:
			raise ValueError("nothing to pop")
			return
		self.head.prev = None	
		self.head = self.head.next

	def top_back(self):
		if self.head is None:
			raise ValueError("nothing to pop")
			return
		node = self.head	
		while node.next is not None:
			node = node.next
		return node.data

	def top_front(self):
		if self.head is None:
			raise ValueError("nothing to pop")
			return
		return self.head.data

	def remove(self, data):
		if  self.head is None:
			raise ValueError("nothing to remove")
			return True
		if self.head.data == data:
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
			raise ValueError("item not in list")			


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

