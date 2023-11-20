"""Node Class."""
from node import Node
__author__ = "730563340" 

class Node:
    """My Node class for linked lists."""

    node_c: Node = Node(2, None) # base case
    node_b: Node = Node(1, node_c)
    node_a: Node = Node(0, node_b) # head of list
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
    print(node_a.next.next.data)
    print(node_a.next.next.next)
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
    print(node_a)
        
    def head(self) -> int:
        print("Actual: ", node_a.head(), " - Expected: 0")
        return None
    
    def tail(self):
        return None
     
    def last(self):
        return None