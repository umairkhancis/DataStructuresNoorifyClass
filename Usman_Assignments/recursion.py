from myarray import MyArray
from doubly_linkedlist import LinkedList

# class Node(object):
#     def __init__(self, data = None, next = None, prev = None):
#         super(Node, self).__init__()
#         self.data = data
#         self.next = next
#         self.prev = prev

#     def __str__(self):
#         return "{} -> {}".format(self.data, self.next)

class Recursion (object):
    def __init__ (self):
        self.array = MyArray('i', 1, 2, 3, 4, 5)
        self.sum = 0
        self.linkedlist = LinkedList()

    # input: n, any non-negative integer
    def print_0toN (self, n):
        if n < 0:
            raise ValueError("Negative input number")
            return

        # 0, 1, 2, 3, 4, 5
        # (5) => (4) => (3) => (2) => (1) => (0) <---- base case (0)
        #  5  <=  4  <=  3  <=  2  <=  1  <=  0 

        # base case
        if n == 0:
            print(n)
            return

        else:
            # Hypothesis
            self.print_0toN(n - 1)
            # Induction
            print(n)
            return

    def print_negative_NtoN(self, n):

    #       -2, -1, 0, 1, 2
    # =================================
    # (2) => (1) => (0) => (-1) => (-2)
    # -2  <= -1  <=  0  <=   1  <=   2

        if N == 0:
            print(n)
            return

        # base case
        if N == -n:
            if n == 0:
                self.print_negative_NtoN(n - 1)
            
            print (n)
            return

        else:
            # Hypothesis
            self.print_negative_NtoN(n - 1)
            # Induction
            print(n)
            return

    

    # print ("print_arr function is running")
    def print_arr (self, arr, start, len):
        
        # base case
        if (start >= len):
            return

        print (self.array.get(start))
        self.print_arr (self.array, start + 1, len)
        return

    def print_reverse_arr(self, arr, end, start):
        # base case
        if (end < start):
            return
        
        print (arr.get(end))
        self.print_reverse_arr(arr, end - 1, start)
        return

    def sumOfArray(self, arr, start):
        if (start >= arr.size()):
            return

        self.sum += arr.get(start)
        self.sumOfArray(arr, start + 1)
        return self.sum

    def print_LinkedList(self, node):
        if node is None:
            return

        print (node.data)
        self.print_LinkedList(node.next)
        return

    def print_reverse_LinkedList(self, node):
        if node is None:
            return

        print (node.data)
        self.print_reverse_LinkedList(node.prev)
        return

    def print_reverse_string(self, string):
        if string == "":
            return

        print (string[0])
        self.print_reverse_string(string[1 : ])

    def isPalindrome(self, string):
        if string == "" or len(string) == 1:
            return True
        if string[0] == string[len(string) - 1]:
            # return True
            return self.isPalindrome(string[1 : len(string) - 1])
        if string[0] != string[len(string) - 1]:
            return False

#             TestCases
# ===================================
N = 5
recursion = Recursion()
# Q1
print ("print_0toN function is running")
recursion.print_0toN (N)
# Q2
print ("print_negative_NtoN function is running")
recursion.print_negative_NtoN (N)
# Q3
print ("print_arr function is running")
recursion.print_arr (recursion.array, 0, recursion.array.size())
# Q4
print ("print__reverse_arr function is running")
recursion.print_reverse_arr (recursion.array, recursion.array.size() - 1, 0)
# Q5
print ("sumOfArray function is running")
print ("sum of elements in array =", recursion.sumOfArray (recursion.array, 0))
# Q6
print ("print_LinkedList function is running")
recursion.linkedlist.push_back(1)
recursion.linkedlist.push_back(2)
recursion.linkedlist.push_back(3)
recursion.linkedlist.push_back(4)
recursion.linkedlist.push_back(5)
recursion.print_LinkedList (recursion.linkedlist.head)
# Q7
print ("print_reverse_LinkedList function is running")
recursion.print_reverse_LinkedList (recursion.linkedlist.tail)
# Q8
print ("print_reverse_string function is running")
recursion.print_reverse_string ("Usman")
# Q9
print ("isPalindrome function is running")
print (recursion.isPalindrome ("madam"))