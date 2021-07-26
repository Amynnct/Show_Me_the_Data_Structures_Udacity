Huffman Coding
In this problem, several classes are being implemented:

- Node: as a element of a binary tree (has two children) and huff property to keep track of the direction
- PriorityQueue: created using a min-heap where if a parent has a index i, then its two children have the indexes of 2i+1 and 2i+2
- HuffmanTree: responsible for building the HuffmanTree and the corresponding encoded dictionary.

Time and Space complexity

ENCODING O(nlogn)

- determine the frequency of each character in the message -> Time O(c) for iterate through each char and space O(n) with n be the number of distinct char. (n <= c)
- iterate through each char and its freq, and add them to the priority queue using enqueue (append takes O(1), bubble_up takes O(logn)) -> O(logn) with n be the number of node with related to the number of distinct char.
- building Huffman Tree: pop-out two nodes with the minimum freq then re-organize the priority queue takes O(2logn) (from sink_down), create a new node O(1), add it to the tree O(1) and reinsert this newly created node back to the priority queue O(logn) -> O(3logn).
  Generally speaking, we pop-out 2 nodes then add in 1 node, almost similar to O(n) and each round we do O(3logn) work => O(nlogn)

DECODING O(n)

- traversing the encoded data from left to right, so the time complexity will depend on the size of the encoded data, which from experiment approximately about half of the orginal data -> O(n)

Space:
O(n) space for the freq dictionary
O(n) space for the priority queue
O(2n-1) or O(n) space for the Huffman Tree (first level has n nodes, second has n/2 nodes, then n/4 nodes,.... until we only have 1 node -> the total is n + n/2 + n/4 + ...+ 1 = 2n - 1)
=> Overall O(n) space
