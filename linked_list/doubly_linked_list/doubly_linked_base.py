class Empty(Exception):
    pass


class _DoublyLinkedBase:
    """
    A base class providing a doubly linked list representation.
    """

    class _Node:
        """
        Lightweight, nonpublic class from storing a doubly linked node.
        """

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """ Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the list.
        """
        return self._size

    def is_empty(self):
        """
        Return True if list is empty.
        :return:
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Add element e between two existing nodes and return new node.
        :param e:
        :param predecessor:
        :param successor:
        :return:
        """
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        Delete nonsentinel node from the list and return its element.
        :param node:
        :return:
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    """
    Double-ended queue implementation based on a doubly linked list.
    """

    def first(self):
        """
        Return (but do not remove) the element at the front of deque.
        :return:
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """
        Add an element to the front of the deque
        :param e:
        :return:
        """
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """
        Add an element of the back of the deque.
        :param e:
        :return:
        """
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        Remove and return the element from the front of deque.
        Raise Empty exception if the deque is empty.
        :return:
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header.next)

    def delete_last(self):
        """
        Remove and return the element from the back of deque.
        Raise Empty exception if the deque is empty.
        :return:
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
