# Binary-Search-Tree
Simple binary search tree implementation in Python. Supports insertion, removal, search, and visualization. [WIP]

# NodeMap Implementation
Initially, I stored each node in a map that direct hashed integer-valued keys corresponding to levels of the tree to float-valued lists containing the keys of nodes in each level. I found this approach helpful when visualizing the tree (as accessing and printing nodes becomes a process of sorting each level's node list, then printing each list line-by-line) and studied its structure to conclude on how if it affected the overall efficiency of the structure's operations.

## Considering the Unbalanced Case

**Runtime Complexity** 


Insertion remains $O(N)$ as, in the worst case, a unbalanced tree would have $N$ levels and an insertion to the corresponding list in the node map requires $1$ operation as each list contains only $1$ element. 

Removal remains $O(N)$, as the worst case requires $O((N - 1) + 1)$ for removing an internal node with $2$ children; each level of the tree is traversed besides the last $(O(N - 1)$, a leaf node cannot have two children), the node's previous key is removed from the map ($O(1)$), its successor's key is appended in the same list ($O(1)$, no resizing), then its successor is recursively removed ($O(1)$, as we search through its parent's subtree for it). Searching and height retrieval both remain the same, as the map is not interacted with in these cases.

**Space Complexity** 


For a tree of height $N - 1$, the corresponding node map is a map of $N$ keys. Each key maps to an integer-valued list of length $1$ and memory allocation of $4$ ([see Python's overallocation method](https://github.com/python/cpython/blob/main/Objects/listobject.c#L46C11-L98)), meaning that the space complexity of storing the node map is $O(4 * 4 * N) = O(N)$. Additionally, we are storing $N$ nodes in the tree itself, where each node contains, at most, $3$ pointers and $1$ integer-valued data member, each of which require $4$ bytes of memory. An unbalanced tree then has space complexity $O((N - 1) * (4 + 4 + 4 + 4) + 1 * (4 + 4)) = O(N)$. Under this implementation, we see that the data structure has total space complexity $O(2N) = O(N)$.

## Considering the Balanced Case

**Runtime Complexity** 


Using previous findings, we can deduce the runtime complexity of traversal by substitution. A balanced tree has $\lfloor log_2(N)\rfloor$ levels, thus the runtime complexity of traversal becomes $O(log(N))$. Insertion remains $O(logN)$ as the insertion to the corresponding list in the node map requires at most $O(2^{level} - 1)$ elements copied under a resizing operation. With amortized analysis, we find that the runtime complexity is, on average, $O(1)$ due to the fact that resizing becomes less and less common as the size of the list grows ([see Python's resizing factor](https://github.com/python/cpython/blob/main/Objects/listobject.c#L46C11-L98)). 


Removal becomes $O(NlogN)$ as each step of removing an internal node with 2 children remains analagous to the unbalanced case, with the only difference stemming from the fact that each list stores at most $2^{level}$ elements and requires $2^{level} - 1$ index shifts in the worst case. This leads to $(2^{level} - 1 + 2^{level + 1} - 1)$ index shifts per removal, given that we remove from the list of one level and the list of the level beneath it. With amortized analysis, we average out the best case with the worst case scenario: the best case is at the top of the tree, requiring $(2^{(0)} - 1 + 2^{(1)} - 1)$ index shifts, and the worst case is at the bottom of the tree, requiring $(2^{log_2(N - 2)} - 1 + 2^{log_2(N - 1)} - 1)$ index shifts. With some algebra, we compute the arithmetic mean finding that our average runtime complexity is $O(N - 2)$ for $N > 2$. This suggests that our runtime complexity for removal increases to linearithmic $O(NlogN)$ in the balanced case, where we expect $O(logN)$.

**Space Complexity** 


For a tree of height $\lfloor log_2(N) - 1\rfloor$, the corresponding node map is a map of $\lfloor log_2(N)\rfloor$ keys. Each key maps to an integer-valued list which has length $2^{level}$ and memory allocation $4$ for $level < 2$ and $2^{level}$ for $level > 2$, giving our space complexity of the node map $O(3 * (4 * 4) + (\lfloor log_2 (N)\rfloor - 3) * (4 * 2^{level}))$. By homogeneity, we can reduce the expression to only its variate terms and find the complexity in terms of $N$: $O(log_2 (N) * 2^{level})$, notice this is an arithmetic series in this form, using the formula for its sum we find $O(log_2 (N) * \frac{2^3 + 2^{log_2 (N)}}{2}) = O(NlogN)$. Because space complexity of a binary tree is proportional to its number of nodes stored, it remains the same as in the unbalanced case $O(N)$, thus we get $O(N + Nlog(N)) = O(Nlog(N))$. 



# Conclusions




