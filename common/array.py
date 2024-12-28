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


    def T(self) -> 'Array[T]':
        new_arr = [[None for _ in range(len(self.arr))] for _ in range(len(self.arr[0]))]
        for x in range(len(self.arr[0])):
            for y in range(len(self.arr)):
                new_arr[x][y] = self.arr[y][x]
        return Array(new_arr)

    def diagonals(self) -> 'List[List[T]]':
        diags = []
        max_y = len(self.arr)
        for y in range(max_y):
            forward_diag = []
            for x in range(y+1):
                y_val = y - x
                if x < len(self.arr[y_val]):
                    forward_diag.append(self.arr[y_val][x])
            diags.append(forward_diag)
            backward_diag = []
            for x in range(max_y-y):
                y_val = y + x
                if x < len(self.arr[y_val]):
                    backward_diag.append(self.arr[y_val][x])
            diags.append(backward_diag)
        for x in range(1, len(self.arr[0])):
            forward_diag = []
            x_val = x
            for y in range(len(self.arr)-1, 0, -1):
                if x_val < len(self.arr[y]):
                    forward_diag.append(self.arr[y][x_val])
                x_val += 1
            diags.append(forward_diag)

            x_val = x
            backward_diag = []
            for y in range(len(self.arr)-1):
                if x_val < len(self.arr[y]):
                    backward_diag.append(self.arr[y][x_val])
                x_val += 1
            diags.append(backward_diag)
        return diags

    def __str__(self) -> str:
        return "\n".join(["".join([str(cell) for cell in row]) for row in self.arr])