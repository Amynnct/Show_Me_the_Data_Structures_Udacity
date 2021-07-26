class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.key_to_node = {}
    
    def enqueue(self, key):
        new_node = Node(key)
        self.key_to_node[key] = new_node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove(self, key):
        node = self.key_to_node[key]
        if node.next is None: #this means the current node is self.tail
            node.prev.next = None
        elif node.prev is None: #this means the curent node is self.head
            self.head = node.next
            node.next.prev = None
        else:  
            node.prev.next = node.next     #make the prev node points to the next node -> skip the current node
            node.next.prev = node.prev
    
    def dequeue(self):
        dequeue_node = self.head
        self.head = self.head.next
        dequeue_key = dequeue_node.key
        return dequeue_key
    
    def print_queue(self):
        current_node = self.head
        while current_node:
            print(f'{current_node.key} ->', end='')
            current_node = current_node.next


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.used_queue = Doubly_Linked_List()
        self.cache = {}
        if capacity <= 0 or capacity is None:
            print("Cache capacity is set to invalid values (null,negative,... etc)")
            return


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            self.used_queue.remove(key)  #remove the previous time we use the key in the queue
            self.used_queue.enqueue(key)  #update the used_queue so that key is the lastest one
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity <= 0:
            print("Invalid operation on null or negative capacity cache.")
            return
        if len(self.cache) >= self.capacity:
            deleted_key = self.used_queue.dequeue()
            del self.cache[deleted_key]
        if key not in self.cache:
            self.cache[key] = value
            self.used_queue.enqueue(key)
        else:    #key in cache
            self.cache[key] = value
            self.used_queue.remove(key)
            self.used_queue.enqueue(key)
        return 

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2

print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 has been removed due to the fact that it's the least recently used
print(our_cache.get(5))      # returns 5
print(our_cache.get(6))      # returns 6

our_cache.set(2, 99)
print(our_cache.get(2))      # returns 99

#Edge cases
our_cache = LRU_Cache(0)     # Cache capacity is set to invalid values (null,negative,... etc)
our_cache.set(1, 1);         # Invalid operation on null or negative capacity cache.
print(our_cache.get(1))      # -1

our_cache = LRU_Cache(-1)    # Cache capacity is set to invalid values (null,negative,... etc)
our_cache.set(2, 2);         # Invalid operation on null or negative capacity cache.
print(our_cache.get(2))      # -1


