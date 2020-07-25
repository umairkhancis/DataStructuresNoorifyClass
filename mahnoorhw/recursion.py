from singly_linkedlist import LinkedList
from myarray import MyArray
# case 1- Given n, print 0 to n
def printnumber(n):
    if n < 1:
        return
    printnumber(n-1)
    print(n)


printnumber(2)

def sumofnumber(n):
    if n <= 1:
        return n
    else:
        return sumofnumber(n-1) + n


print(sumofnumber(4))



def rprintnumber(n):
    if n < 1:
        return
    print(n)
    rprintnumber(n - 1)


#rprintnumber(2)
# case 2 Given n, print -n to n
def nnumber(n):

    if n < 0:
        return
    print(-1*n)
    nnumber(n - 1)
    print(n)

nnumber(3)
def number_nto0(n):

    if n < 0:
        return
    print(-1 * n)
    number_nto0(n - 1)


def negtopos(n):

    number_nto0(n)
    printnumber(n)

negtopos(4)

#case 3 Given arr, print all elements of array.
arri = MyArray('i', 2,3,4,5,6)
#print(arri.size())
arr= [2,3,4,4,5]
print(arr)
print(arr[::-1])
#for i in arr:
#print(i)
#print(arr[0])
def array_(arr):
    if len(arr) == 0:
        return arr
    print(arr[0])
    array_(arr[1:])

print(array_([2, 4, 5, 6]))



#4- Given arr, print all elements in reverse order.
def rarray_(arr):
    if len(arr) == 0:
        return
    rarray_(arr[1:])
    print(arr[0])


print(rarray_([2, 4, 5, 6]))

#5- Given arr, print sum of all elements in array.
def array_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + array_sum(arr[1:])


print(array_sum([2, 4, 5, 6]))
#7- Given a linkedlist, print all of its elements.
linkedlist =  LinkedList()
linkedlist.push_back("A")
linkedlist.push_back("M")
linkedlist.push_back("U")
linkedlist.push_back("H")
def linklist_print(curr):
    if (curr == None):
        return
    print(curr.data)
    linklist_print(curr.next)

linklist_print(linkedlist.head)
#8- Given a linkedlist, print all of its in reverse order elements without reversing the links.
def rlinklist_print(curr):
    if (curr == None):
        return

    rlinklist_print(curr.next)
    print(curr.data)

rlinklist_print(linkedlist.head)

def printstring(st):
    if len(st) == 0:
        return
    print(st[0])
    printstring(st[1:])
a = str(input("Enter the string to be print "))
printstring(a)
#9- Given a string, print it in reverse order.
def reversestring(string):
    if len(string) == 0:
        return string
    else:
        return reversestring(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reversestring(a))

def notreversestring(string):
    if len(string) == 0:
        return string
    else:
        return string[0] + notreversestring(string[1:])
a = str(input("Enter the string to be print: "))
print(notreversestring('a'))


def isPalRecursion(st, s, e):
    if (s == e):
        return True

    if (st[s] != st[e]):
        return False

    if (s < e + 1):
        return isPalRecursion(st, s + 1, e - 1);

    return True


def isPalindrome(st):
    n = len(st)
    if (n == 0):
        return True

    return isPalRec(st, 0, n - 1);

st = "geeg"
if (isPalindrome(st)) :
    print('true')
else :
    print('false')