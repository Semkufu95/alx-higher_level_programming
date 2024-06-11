#!/usr/bin/python3

'''A class that defines node of a singly linked list '''


class Node:
    '''defines the node'''

    def __init__(self, data, next_node=None):
        ''' initializes the "data" and "next_node" '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''retrieves data'''
        return self.__data

    @data.setter
    def data(self, value):
        ''' sets a new value to a node '''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        '''retrieves the next node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''sets e new next node'''
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    '''Defines singly linked list  class'''
    def __init__(self):
        '''initiates the singly linked list'''
        self.__head = None

    def __str__(self):
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        ''' inserts a new node in a singly linked list'''
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

