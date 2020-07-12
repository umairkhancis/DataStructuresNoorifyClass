from doubly_linkedlist import *

class Queue(object):
	def __init__(self):
		self.linkedlist = LinkedList()

	def push(self, data):
		return self.linkedlist.push_back(data)	 	

	def pop(self):
		return self.linkedlist.pop_front()

	def top(self):
		return self.linkedlist.top_front()

	def isEmpty(self):
		if self.linkedlist.head is None:
			return True
		else:
			return False	

	def size(self):
		return self.linkedlist.size()