For LRU cache, we need to keep track of the recently used entry, the least recently used will be the first one to pop out. Thus, if we didn't reuse the entry then the first one we used should be the first one we pop (to delete). -> Using a queue

When the entry is used again, remove that entry from the queue and add it again so that it becomes the most recently used. Because our queue needs to perform delete operation quickly O(1), using a array is not a good idea. -> use a doubly linked list to implement our used_queue.

We would like to delete a node corresponding to a specify entry without tranverse through the entire linked list. To do that, we can keep a hashmap that maps the entries with corresponding nodes. -> key_to_node hmap

Time and Space complexity
get -> used_queue remove() access node using the key O(1), delete the node O(1) (doubly linked list properties), enqueue O(1) => Overall Time O(1)

set -> dequeue easily by accessing self.head O(1), delete key in hmap and cache O(1) (hashmap properties) => Overall Time O(1)

Space O(n) for hmap with n be the capactity -> doesn't change depending on num of input -> O(1)
