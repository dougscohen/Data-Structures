"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from singly_linked_list.singly_linked_list import LinkedList, Node

        
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

        self.front = None
        self.rear = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add element to LL's tail and incrase size by 1
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        # if LL is empty, do nothing
        if self.size == 0:
            return None
        # if LL is not empty, decrease size by 1 and remove head (FIFO)
        else:
            self.size -= 1
            return self.storage.remove_head()

