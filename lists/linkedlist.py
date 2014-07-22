#! /usr/bin/env python3





class LinkedList(object):
    """ Implementation of a linked list """

    
    class _Node(object):

        """ Node of linked list """
        

        __slots__ = ['value', 'follower']


        def __init__(self, value, follower):

            self.value = value
            self.next = follower


    def __init__(self):
        
        self._length = 0
        self._head = None
        self._tail = None

    def __len__(self):
        """ Returns the length of the linked list """
        return self._length

    def __contains__(self, node):
        """ Returns true if node is in linked list """

        nd = self._head
        if self.is_empty:
            return False

        while nd is not None:
            if nd == Node:
                return True

        return False


    def is_empty(self):
        return self._length == 0

    def first(self):
        return self.head()
    def head(self):
        return self._head
    def last(self):
        return self.tail()
    def tail(self):
        return self._tail

    def length(self):
        return self._length
    
    def before(self, node):
        """ Returns the node before the given node. If given node is head node, returns None. Otherwise raises error"""
         nd = self._head
        while nd is not None:
            if nd.next == node:
                return nd
        if nd is None:
            # Was the given node the head node?
            if self._head == node:
                return None
            else:
                # Otherwise node must not belong in list
                raise ValueError("Given node not a member of this linked list")
    def get_node(self, node):
        """ Returns the given node. If node is not in list, returns error """

        nd = self._head
        if self.is_empty:
            return IndexError("Linked List is empty")

        while nd is not None:
            if nd == Node:
                return nd

        return ValueError("Given node is not a member of this linked list")
        
    
    def add_after(node, value):
        """ Add new node with given value after given node
        """
        
        #Sanity check
        if node not in self:
            raise ValueError("Given node not a member of this linked list")
        
        # if tail, should maintain reference to None
        nxt = node.next
        node.next = _Node(value, nxt)

        # If given node was tail, change reference...
        if self._tail == node:
            self._tail = node.next
        
        # Don't forget to increase the object length!
        self._length += 1

    def add_before(node, value):
        """ Add new node with given value before given node """
        nd = self.before(node)
        new_node = _Node(value, node)
        if nd is not None:
            nd.next = new_node
            new_node.next = node
        else:
            # Was the given node the head node?
            if self._head == node:
                self._head = new_node
        
        # Don't forget to increase the object length!
        self._length += 1

    def append(self,value):
        """ Adds new node to end of linked list """

        self.add_after(self._tail, value)


    def prepend(self,value):
        """ Adds new node to start of linked list """

        self.add_before(self._head, value)

    def pop(self, node = None)
        """ Removes given node, or tail node (if no node is given) """
    
        if node is None:
            node = self._tail
             
        if node == self._head:
            self._head = node.next
            node.next = None
        else:
            nd = self.before(node)
            if node == self._tail:
                self._tail = nd
                nd.next = None
            else:
                nd.next = node.next
                node.next = None
        
        self._length -= 1
        return node




