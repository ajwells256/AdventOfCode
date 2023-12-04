from typing import Callable,Dict,Generic,List,Tuple,TypeVar

T = TypeVar("T")

class Array(Generic[T]):
    def __init__(self, arr: List[List[T]]):
        self.arr: List[List[T]] = arr

    # left to right, top to bottom
    def foreach_neighbor(self, func: Callable[[Tuple[int,int,T], List[Tuple[int,int,T]], Dict[str, object]], None], diagonals: bool = False, memo: Dict[str, object] = {}):
        steps = [(1,0), (0,1), (-1,0), (0,-1)]
        if diagonals:
            steps += [(1,1), (1,-1), (-1,1), (-1,-1)]
        for y in range(len(self.arr)):
            for x in range(len(self.arr[0])):
                neighbors = []
                for step in steps:
                    dx,dy = step
                    if x+dx >= 0 and y+dy >= 0 and x+dx < len(self.arr[0]) and y+dy < len(self.arr):
                        neighbors.append((dx,dy,self.arr[y+dy][x+dx])) 
                func((x,y,self.arr[y][x]), neighbors, memo)
                
