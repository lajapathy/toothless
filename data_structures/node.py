"""Node class."""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def add_next(self, node):
        self.next = node

    def get_next(self):
        return self.next
