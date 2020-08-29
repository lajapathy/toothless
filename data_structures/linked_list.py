"""LinkedList class."""

from lib import error
from data_structues.node import Node


class LinkedList(Node):
    def __init__(self, head):
        self.head = self._create_node(head)

    def _create_node(self, val):
        if isinstance(val, int):
            return Node(val)
        elif isinstance(val, Node):
            return val
        raise error.TestError('Invalid linkedlist head type')

    def add_node_tail(self, node):
        pass

    def add_node_position(self, node, position):
        pass

    def delete_node(self, val):
        pass


