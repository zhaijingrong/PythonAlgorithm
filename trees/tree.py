class Tree:
    """
    Abstract base class representing a tree structure.
    """

    class Position:
        """
        An abstraction representing the location of single element.
        """
        def element(self):
            """
            Return the element sotred at this Position.
            :return:
            """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """
            Return True if other Position represents the same location.
            :param other:
            :return:
            """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """
            Return True if other does not represent the same location.
            :param other:
            :return:
            """
            return not(self == other)

    def root(self):
        """
        Return Position representing the tree's root(or None if empty)
        :return:
        """
        raise NotImplementedError('must be implemented by subclass')
