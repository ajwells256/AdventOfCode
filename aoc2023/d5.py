from typing import List,Set,Tuple
from re import findall,match

from common.preader import read_lines
from common.logger import log

seed_soil = 0
soil_fert = 1
fert_wat = 2
wat_lit = 3
lit_temp = 4
temp_hum = 5
hum_loc = 6

def parse_almanac(lines) -> Tuple[List[int], List[List[Tuple[int,int,int]]]]:
    seeds: List[int] = []
    maps: List[List[Tuple[int, int, int]]] = []
    for i in range(hum_loc + 1):
        maps.append([])

    cur_map = -1
    for l in lines:
        if len(l) == 0:
            continue
        elif "seeds:" in l:
            seeds = list(map(int, l.replace("seeds: ", "").split(" ")))
        elif "seed-to-soil" in l:
            cur_map = seed_soil
        elif "soil-to-fert" in l:
            cur_map = soil_fert
        elif "fertilizer-to-water" in l:
            cur_map = fert_wat
        elif "water-to-light" in l:
            cur_map = wat_lit
        elif "light-to-temp" in l:
            cur_map = lit_temp
        elif "temperature-to-humi" in l:
            cur_map = temp_hum
        elif "humidity-to-loc" in l:
            cur_map = hum_loc
        else: 
            try: 
                maps[cur_map].append(tuple(map(int, l.split(" "))))
                assert len(maps[cur_map][-1]) == 3
            except:
                print(f"Parse of {l} into map failed")

    return (seeds, maps)

def alm_map(map_rules, value, backwards=False) -> (int,int):
    def unwrap(m):
        if backwards:
            dst,src,l = m
            return (src,dst,l)
        return m
    
    res = value
    width = 2**32
    min_next_rule = 2**32
    for m in map_rules:
        dst,src,l = unwrap(m)
        if value < src and src < min_next_rule:
            min_next_rule = src
            width = src - value
        elif src <= value and value < src + l:
            offset = value - src
            res = dst + offset
            width = l - offset 
            log.vdebug(f"Mapped {value} to {res} width {width} through rule {m} (backwards: {backwards})")
            break
    return (res, width)

def loc_to_seed(all_maps, loc) -> int:
    val = loc
    for i in range(hum_loc, -1, -1):
        val,_ = alm_map(all_maps[i], val, True)
    return val

def seed_to_loc(all_maps, seed) -> int:
    val = seed
    for i in range(hum_loc + 1):
        val,_ = alm_map(all_maps[i], val)
    return val

def part1(sample: bool = False) -> int:
    p = read_lines(5,1,sample)
    seeds, maps = parse_almanac(p)
    return min(map(lambda x: seed_to_loc(maps, x), seeds))   

def map_ranges(all_maps, ranges: List[Tuple[int,int]], i=0) -> List[Tuple[int,int]]:
    if i > hum_loc:
        return ranges
    
    mapped_ranges = []
    for r in ranges:
        idx,l = r
        while l > 0:
            new_idx,width = alm_map(all_maps[i], idx)
            mapped_ranges.append((new_idx, min([width, l])))
            log.vdebug(f"Mapped range {r} to {mapped_ranges[-1]}")
            idx += width
            l -= width
    return map_ranges(all_maps, mapped_ranges, i+1)

def part2(sample: bool = False) -> int:
    p = read_lines(5,1,sample)
    raw_seed_ranges, maps = parse_almanac(p)

    seed_ranges: List[Tuple[int,int]] = []
    for i in range(0, len(raw_seed_ranges), 2):
        seed_ranges.append((raw_seed_ranges[i], raw_seed_ranges[i+1]))    

    return min(map_ranges(maps, seed_ranges), key=lambda x: x[0])[0]

if __name__ == "__main__":
    if "part2" not in globals():
        print(part1())
    else:
        print(part2())

