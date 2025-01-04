from Graph.Node.Node import Node
from Queue.Deque.Deque import Deque
from typing import TypeVar, Callable, Optional

T = TypeVar("T")

def bfs(
    start: Node[T],
    process_fn: Optional[Callable[[Node[T]], None]] = None,
    enqueue_fn: Optional[Callable[[Node[T]], None]] = None,
) -> None:
    """
    Breadth-First Search (BFS) using a set for tracking visited nodes.
    :param start: The starting node.
    :param process_fn: Function to execute when dequeuing a node.
    :param enqueue_fn: Function to execute when adding a node to the queue.
    """
    if start is None:
        return

    # Initialize the queue and visited set
    queue = Deque([start])
    visited = set()

    # Mark the starting node as visited
    visited.add(start)

    # Optionally execute enqueue function for the starting node
    if enqueue_fn:
        enqueue_fn(start)

    # Process the queue until it's empty
    while queue:
        # Remove the front node from the queue
        node = queue.remove_front()

        # Execute the processing function when dequeuing the node
        if process_fn:
            process_fn(node)

        # Add all unvisited adjacent nodes to the queue
        for adjacent in node.adjacent_nodes:
            if adjacent not in visited:
                queue.add_rear(adjacent)
                visited.add(adjacent)

                # Execute the enqueue function when enqueuing the node
                if enqueue_fn:
                    enqueue_fn(adjacent)


def dfs(
    node: Optional[Node[T]],
    pre_fn: Optional[Callable[[Node[T]], None]] = None,
    post_fn: Optional[Callable[[Node[T]], None]] = None,
    visited: Optional[set[Node[T]]] = None
) -> None:
    """
    Depth-First Search (DFS) using a set for tracking visited nodes.
    :param node: The starting node
    :param pre_fn: Function to execute when first visiting the node.
    :param post_fn: Function to execute during backtracking from the node.
    :param visited: A set to track visited nodes.
    """
    if node is None:
        return

    if visited is None:
        visited = set()

    if node in visited:
        return

    # Mark the current node as visited
    visited.add(node)

    # Execute the pre-processing function, if provided
    if pre_fn:
        pre_fn(node)

    # Recursively visit all unvisited adjacent nodes
    for adjacent in node.adjacent_nodes:
        if adjacent not in visited:
            dfs(adjacent, pre_fn, post_fn, visited)

    # Execute the post-processing function, if provided
    if post_fn:
        post_fn(node)


