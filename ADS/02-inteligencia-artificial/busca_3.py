"""Busca A* em uma grade com custos uniformes e heurística Manhattan."""
from __future__ import annotations
import argparse, heapq, json
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True, order=True)
class Node:
    f: int
    g: int
    pos: tuple[int,int]

def manhattan(a: tuple[int,int], b: tuple[int,int]) -> int:
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def astar(grid: list[str], start: tuple[int,int], goal: tuple[int,int]) -> dict:
    if not grid or any(len(row)!=len(grid[0]) for row in grid): raise ValueError('grade vazia ou irregular')
    h,w=len(grid),len(grid[0])
    def valid(p): return 0<=p[0]<h and 0<=p[1]<w and grid[p[0]][p[1]]!='#'
    if not valid(start) or not valid(goal): raise ValueError('origem/destino bloqueado ou fora da grade')
    frontier=[Node(manhattan(start,goal),0,start)]; came={start:None}; cost={start:0}; expanded=0
    while frontier:
        node=heapq.heappop(frontier); current=node.pos; expanded+=1
        if current==goal: break
        for nxt in ((current[0]-1,current[1]),(current[0]+1,current[1]),(current[0],current[1]-1),(current[0],current[1]+1)):
            if not valid(nxt): continue
            new_cost=cost[current]+1
            if new_cost<cost.get(nxt,10**9):
                cost[nxt]=new_cost; came[nxt]=current
                heapq.heappush(frontier,Node(new_cost+manhattan(nxt,goal),new_cost,nxt))
    if goal not in came: return {'found':False,'path':[],'cost':None,'expanded_nodes':expanded}
    path=[]; p=goal
    while p is not None: path.append(p); p=came[p]
    path.reverse(); return {'found':True,'path':path,'cost':cost[goal],'expanded_nodes':expanded}

def demo(): return astar(['....','.##.','....'],(0,0),(2,3))
if __name__=='__main__': print(json.dumps(demo(),ensure_ascii=False))
