'''
3.6
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data structure.
Hints: #22, #56, #63
'''
import time


class Node:
    def __init__(self, data, next = None):
        self.next = next
        self.data = data

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, node):
        if self.head is None:
            self.head = node
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                current.next = node

    def pop(self):
        if self.head is not None:
            head_node = self.head
            self.head = self.head.next
            return head_node
        return None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count
        
class Animal:
    def __init__(self, name):
        self.time_admitted = time.time()
        self.name = name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter(LinkedList):
    def enqueue(self, animal):
        animal_node = Node(animal)
        self.insert(animal_node)

    def dequeue_any(self):
        return super().pop()
    
    def dequeue_cat(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if isinstance(current_node.data, Cat):
                previous_node.next = current_node.next 
                return current_node.data
            previous_node = current_node
            current_node = current_node.next
            
