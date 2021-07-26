Due to Blockchain nature, in this problem blockchain is being implemented with a similarity to linked list:

- Blockchain's elements are Blocks just like how Nodes are elements of a normal Linked List. However, instead of pointing to the next Block, each Block stores the previous's Block hash.
- new_transaction is similar to append operation. O(1)
- last_transaction is similar to peak operation. O(1)
- transcation_list is similar to print_linked_list function. O(n)
- search_transcation is similar to search operation. O(n)

Nonetheless, there are some methods that available for linked list but not for blockchain (Ex: prepend, remove, insert, pop,...). This assures the immutability feature of Blockchain, makes blockchain cannot be changed or altered once created.

For Space complexity, it takes O(n) for the number of nodes or transactions that have occured.
