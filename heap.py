# helper functions

def left(index):
    '''Return index's left child index.
    '''
    return index * 2 + 1


def right(index):
    '''Return index's left child index.
    '''
    return index * 2 + 2
    
    
def parent(index):
    '''Return index's parent index.'''
    
    return (index - 1) // 2


class MinHeap:
    
    def __init__(self, L=None):
        '''Create a new MinHeap.
        This method is complete.'''
        
        if not L:        
            self._data = []
        else:
            self._data = L
            self._min_heapify()

        
    def __len__(self):
        '''Return the length of the MinHeap.
        This method is complete.'''
        
        return len(self._data)
    

    def __str__(self):
        '''Return a string representation of the heap.
        This method is complete.'''
        
        return str(self._data)
    
    
    def insert(self, v):
        '''Insert v in self. Maintain heap property.'''
        
        self._data.append(v)
        if len(self._data) == 1: return
        self._percolate_up(len(self._data)-1)
    
    
    def extract_min(self):
        '''Remove minimal value in self. Restore heap property.
        Raise EmptyHeapException if heap is empty.'''
        
        if len(self._data) == 0: raise EmptyHeapException()
        result = self._data[0]
        if len(self._data) == 1: 
            self._data = []
            return result
        
        self._data[0] = self._data[-1]
        del self._data[-1]
        self._percolate_down(0)
        return result
    
    def _percolate_up(self, i):
        '''Restore heap property of self after 
        adding new item'''
        
        p = parent(i)
        if self._data[i] < self._data[p]: self._swap(p,i)
        
        if p != 0: self._percolate_up(p)
    
    
    def _percolate_down(self, i):
        ''' Restore heap property of subtree 
        rooted at index i.
        '''
        
        # while larger than at least one child
        # swap with smaller child and repeat    
        if left(i) < len(self._data): 
            self._percolate_down(left(i))
            if self._data[i] > self._data[left(i)]: self._swap(i, left(i))
        if right(i) < len(self._data): 
            self._percolate_down(right(i))
            if self._data[i] > self._data[right(i)]: self._swap(i, right(i))

    
    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''
        
        # for each node in the first half of the list
        # percolate down
        half = len(self._data)//2 -1
        for i in range(half, -1, -1):
            self._percolate_down(i)

    
    def _swap(self, a, b):
        temp = self._data[a]
        self._data[a] = self._data[b]
        self._data[b] = temp

class EmptyHeapException(Exception):
    def __init__(self):
        super().__init__("Heap is empty")