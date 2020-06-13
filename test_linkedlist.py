import unittest
from linkedlist import LinkedList

class LinkedListTests(unittest.TestCase):
	def test_size_when_empty_linkedlist(self):
		# Arrange
		linkedlist = LinkedList()
		
		# Act
		size = linkedlist.size()

		# Assert
		self.assertEqual(0, size)

	def test_size_when_single_item_linkedlist(self):
		linkedlist = LinkedList()
		linkedlist.append("Umair")
		
		# Act
		size = linkedlist.size()

		# Assert
		self.assertEqual(1, size)

	def test_size_when_two_items_linkedlist(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")
		linkedlist.append("Aamir")
		
		# Act
		size = linkedlist.size()

		# Assert
		self.assertEqual(2, size)

	def test_size_when_more_than_two_items_linkedlist(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Aamir")
		linkedlist.append("Maria")
		linkedlist.append("Umair")
		linkedlist.append("Usman")

		# Act
		size = linkedlist.size()

		# Assert
		self.assertEqual(4, size)

	def test_find_when_item_is_present(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")

		# Act
		found = linkedlist.find("Umair")

		# Assert
		self.assertTrue(found)
		self.assertEqual("Umair", found.data)

	def test_find_when_item_is_not_present(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")

		# Act
		found = linkedlist.find("Usman")

		# Assert
		self.assertFalse(found)

	def test_update_when_item_is_present(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")

		# Act
		updated = linkedlist.update("Umair", "Usman")

		# Assert
		self.assertTrue(updated)
		self.assertTrue(linkedlist.find("Usman"))

	def test_update_when_item_is_not_present(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")

		# Act
		updated = linkedlist.update("Usman", "Aamir")

		# Assert
		self.assertFalse(updated)
		self.assertFalse(linkedlist.find("Aamir"))

	def test_remove_when_item_is_present_and_head_item_is_deleted_when_list_is_only_one_item(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")

		# Act
		removed = linkedlist.remove("Umair")

		# Assert
		self.assertTrue(removed)
		self.assertFalse(linkedlist.find("Umair"))
		self.assertTrue(linkedlist.size() == 0)

	def test_remove_when_item_is_present_and_head_item_is_deleted_when_list_is_more_than_one_item(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")
		linkedlist.append("Aamir")
		linkedlist.append("Usman")

		# Act
		removed = linkedlist.remove("Umair")

		# Assert
		self.assertTrue(removed)
		self.assertFalse(linkedlist.find("Umair"))
		self.assertTrue(linkedlist.size() == 2)

	def test_remove_when_item_is_present_and_non_head_middle_item_is_deleted_when_list_is_more_than_one_item(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")
		linkedlist.append("Aamir")
		linkedlist.append("Usman")

		# Act
		removed = linkedlist.remove("Aamir")

		# Assert
		self.assertTrue(removed)
		self.assertFalse(linkedlist.find("Aamir"))
		self.assertTrue(linkedlist.size() == 2)

	def test_remove_when_item_is_present_and_non_head_last_item_is_deleted_when_list_is_more_than_one_item(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")
		linkedlist.append("Aamir")
		linkedlist.append("Usman")

		# Act
		removed = linkedlist.remove("Usman")

		# Assert
		self.assertTrue(removed)
		self.assertFalse(linkedlist.find("Usman"))
		self.assertTrue(linkedlist.size() == 2)

	def test_remove_when_item_is_not_present_when_list_is_more_than_one_item(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")
		linkedlist.append("Aamir")
		linkedlist.append("Usman")

		# Act
		removed = linkedlist.remove("Maria")

		# Assert
		self.assertFalse(removed)
		self.assertFalse(linkedlist.find("Maria"))
		self.assertTrue(linkedlist.size() == 3)

	def test_reverse_when_list_is_empty(self):
		# Arrange
		linkedlist = LinkedList()

		# Act
		linkedlist.reverse()

		# Assert
		self.assertFalse(linkedlist.head)

	def test_reverse_when_list_is_only_one_item(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")

		# Act
		linkedlist.reverse()

		# Assert
		self.assertTrue(linkedlist.head and linkedlist.head.data == "Umair")

	def test_reverse_when_list_is_two_items(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")
		linkedlist.append("Aamir")

		# Act
		linkedlist.reverse()

		# Assert
		self.assertTrue(linkedlist.head and linkedlist.head.data == "Aamir")

	def test_reverse_when_list_is_more_than_two_items(self):
		# Arrange
		linkedlist = LinkedList()
		linkedlist.append("Umair")
		linkedlist.append("Aamir")
		linkedlist.append("Usman")

		# Act
		linkedlist.reverse()

		# Assert
		self.assertTrue(linkedlist.head and linkedlist.head.data == "Usman")
