from re import match

from common.preader import read_array
from common.array import Array
from common.logger import log

def find_part_numbers(current, neighbors, memo):
    # initialize memo
    if "vp" not in memo: # valid part flag
        memo["vp"] = False
    if "sb" not in memo: # string builder
        memo["sb"] = ""
    if "parts" not in memo:
        memo["parts"] = []

    #part 2
    if "p" not in memo: # part, (x,y, symbol)
        memo["p"] = (0,0,'c')
    if "gears" not in memo:
        memo["gears"] = {} # dict of gear (x,y) to values

    x,y,c_val = current
    # part number parsing is done, via newline or end of number
    # either way, document the part number if it was valid
    if not match("\d", c_val) or x == 0:
        if len(memo["sb"]) > 0 and memo["vp"]:
            part_num = int(memo["sb"])
            memo["parts"].append(part_num) 
            px,py,p_val = memo["p"]
            if p_val == "*":
                cord = (px,py)
                if cord in memo["gears"]:
                    memo["gears"][cord].append(part_num)
                else:
                    memo["gears"][cord] = [part_num] 
        memo["sb"] = ""
        memo["vp"] = False
    
    if c_val != '.':
        if match("\d", c_val):
            memo["sb"] += c_val
            
            # look for a part in the vicinity of this number
            # only if it's not already validated as a part number
            if not memo["vp"]:
                for n in neighbors:
                    dx,dy,n_val = n
                    if match("[^0-9.]", n_val):
                        memo["vp"] = True
                        memo["p"] = (x+dx,y+dy,n_val)

def part1(sample: bool = False) -> int:
    arr = Array(read_array(3, 1, sample))
    memo = {}
    arr.foreach_neighbor(find_part_numbers, diagonals=True, memo=memo)
    log.debug(memo["parts"])
    return sum(memo["parts"])

def part2(sample: bool = False) -> int:
    arr = Array(read_array(3, 1, sample))
    memo = {}
    arr.foreach_neighbor(find_part_numbers, diagonals=True, memo=memo)
    log.debug(memo["gears"])
    run_sum = 0
    for cord,vals in memo["gears"].items():
        if len(vals) == 2:
            run_sum += vals[0]*vals[1]
    return run_sum


if __name__ == "__main__":
    if "part2" not in globals():
        print(part1())
    else:
        print(part2())
