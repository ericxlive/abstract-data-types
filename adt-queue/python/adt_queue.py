""" This class represents a Queue Node to store values and also
    links others Nodes with values."""
class Node:

    """ It starts with a value at all times. A note can not be
        created without a value associated. """
    def __init__(self, value):
        self.value = value
        self.next = None

""" This class represents a Queue to store values. The Queue starts
    with a node called head. Every single element is going to be added
    after the last node entered."""
class Queue:

    """ The Queue is created with it's size zero and the head element
        head is None (undefined)."""
    def __init__(self):
        self.head = None
        self.size = 0

    """ It adds a new value. The value is going to be added always after the
        last value added. If the Queue has no elements, the value added is
        going to be the head/head and also the last/tail value."""
    def enqueue(self, value):
        if (self.head is None):
            self.head = Node(value)
            self.size += 1
        else:
            pointer = self.head
            while(pointer.next is not None):
                pointer = pointer.next
            pointer.next = Node(value)

    """ This routine removes and also returns the first element. After the
        remotion of the element, the head is updated and it turns to be the next
        element of the queue (it's next element). If there are no more elements
        other than the head, the Queue turns to be empty. If there are no elements
        at all, there will be no remotion or return."""
    def dequeue(self):
        if (self.head is not None):
            removed = self.head.value
            self.head = self.head.next
            self.size -= 1
            return removed

    """ It shows all the Queue elements one by one in a correct
        order. """
    def display(self):
        pointer = self.head
        while (pointer is not None):
            print pointer.value
            pointer = pointer.next

    """ It returns the head node value, but it doesn't remove the
        node. """
    def head(self):
        return self.head.value

    """ It verifies whether or not the Queue has elements. If the Queue
        doesn't have any elements, the head or head element is going to
        be None. """
    def is_empty(self):
        return self.head is None
