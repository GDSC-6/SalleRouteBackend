class Node:
    def __init__(self, id: str, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y

class Edge:
    def __init__(self, source: str, target: str, weight: int):
        self.source = source
        self.target = target
        self.weight = weight