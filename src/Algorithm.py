from collections import deque
import math
class Algorithm:
    def __init__(self):
        self.cost = 0
        self.heuristic = {
            'A': 18,
            'B': 17,
            'C': 15,
            'D': 16,
            'E': 14,
            'F': 13,
            'G': 12,
            'H': 13,
            'I': 11,
            'J': 10,
            'K': 9,
            'L': 9,
            'M': 10,
            'N': 8,
            'O': 7,
            'P': 6,
            'Q': 6,
            'R': 5,
            'S': 4,
            'T': 4,
            'U': 3,
            'V': 2,
            'W': 1,
            'X': 2,
            'Y': 1,
            'Z': 0
            }
        self.path = []
        self.total = 0
    
    def run_algorithm(self, graph):
        visited = set()
        queue = deque()
        queue.append('A')
        self.cost_so_far = 0
        curr_gn = 0
        
        previous_gn = 0
        previous_hn = 0

        while len(queue) > 0:
            curr_fn = math.inf

            curr = queue.popleft()
            self.path.append(curr)

            if not graph[curr]: return

            for node, weight in graph[curr]:
                if node not in visited:
                    visited.add(node)
                    gn = weight + self.cost_so_far
                    hn = self.heuristic[node]
                    fn = gn + hn
                    if fn < curr_fn:
                        curr = node
                        curr_fn = fn
                        curr_gn = gn
            

            queue.append(curr)
            self.cost_so_far = curr_gn
    
    def print_path(self):
        print("-------------------------------------")
        print("Path: ")
        for node in self.path:
            if node == self.path[len(self.path) - 1]:
                print(node)
            else:
                print(node, end=" -> ")
        print("Path Cost: ", end="") 
        print(self.cost_so_far)
        print("-------------------------------------")