'''Heap Class'''


class Heap(object):
    '''Heap Class'''
    def __init__(self):
        self.heap = []
        self.heap_length = 0

    def get_left_child(self, curr_pos):
        '''
        Returns left child position
        Args:
          curr_pos(int): position of parent
        '''
        return 2*curr_pos

    def get_right_child(self, curr_pos):
        '''
        Returns right child position
        Args:
          curr_pos(int): position of parent
        '''
        return 2*curr_pos+1

    def get_parent(self, pos):
        '''Returns index of parent.'''
        return pos//2

    def insert(self, element):
        '''Inserts element at end of heap and runs min-heapify'''
         self.heap.append(element)
         self.heap_length+=1
         self.heapify()

    def is_leaf(self, curr_pos):
        '''Checks if element at given position is leaf or not.'''
        return False if curr_pos >= (
            self.heap_length//2) and curr_pos <= self.heap_length  else True

    def heapify(self, pos):
        '''Runs heapify starting from given position
        Args:
          pos(int): position to start heapify from
        '''
        if is_leaf(pos):
            return
        parent = self.heap[pos]
        lchild = self.heap[self.get_left_child]
        rchild = self.heap[self.get_rightt_child]
        while(pos<=self.heap_length):
            if parent > lchild:
                parent, lchild = lchild, parent
                self.heapify(self.get_left_child)
            else:
                parent, rchild = rchild, parent
                self.heapify(self.get_right_child)
       
                self.heap[pos], self.heap[]
        

