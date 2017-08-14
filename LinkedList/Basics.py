#Import Packages 
import numpy as np

# Single Node in linked list
class Node(object):
	def __init__(self,value):
		self.value = value	
		self.next = None
#Linked List 
class LinkedList(object):
	#constructor make track of head
	def __init__(self,head=None):
		self.head = head
	
	#Append a new node to the list
	def append(self,new_node):
		current = self.head
		if current:
			while current.next:
				current = current.next
			current.next = new_node
		else:
			self.head = new_node

        """Get an element from a particular position.
       	Assume the first position is "1".
        Return "None" if position is not in the list."""
	def get_position(self,position):
        	current = self.head 
        	pos = 1
        	if position < 1 :
        		return None
        	if current :	
            		while current and pos < position :
                		current = current.next
                		pos = pos+1
            		if pos == position :
                		return current
        	return None
	
	"""Insert a new node at a given position.
	Assume the first position is 1.
	Inserting at position 3 means between the 2nd and 3rd element."""
	def insert(self,new_node,position):
		current = self.head
		pos = 1
		if position<1 :
			return None
		if current :
			while current and pos<(position-1):
				current = current.next
				pos = pos+1
			if pos == position :
				new_node.next = current.next
				current.next = new_node
			elif position==1 :
				new_node.next = self.head
				self.head = new_node
		else :
			return None

	def delete(self, value):
        	"""Delete the first node with a given value."""
        	current = self.head
		previous = None
        	while current.value != value and current.next:
			previous = current
			current = current.next
		if current.value == value :
			if previous :
				previous.next = current.next
			else :
				self.head = current.next

	#Display list
	def display(self):
		print 'Calling Display Function'
		current = self.head
		while current:
			print current.value
			current = current.next
		
#Main Function
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

LL1 = LinkedList()
LL1.append(node1)
LL1.append(node2)
print LL1.get_position(1).value
LL1.display()
