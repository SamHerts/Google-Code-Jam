"""
You have just entered the world's easiest maze. You start in the northwest cell of an N by N grid of unit cells, 
and you must reach the southeast cell. You have only two types of moves available: a unit move to the east, 
and a unit move to the south. You can move into any cell, but you may not make a move that would cause you to leave the grid.

You are excited to be the first in the world to solve the maze, but then you see footprints. 
Your rival, Labyrinth Lydia, has already solved the maze before you, using the same rules described above!

As an original thinker, you do not want to reuse any of Lydia's moves. Specifically, if her path includes a unit move from some cell A 
to some adjacent cell B, your path cannot also include a move from A to B. 
(However, in that case, it is OK for your path to visit A or visit B, as long as you do not go from A to B.) Please find such a path.

Sample Input:
2 -- number of tests
2 -- side length of maze
SE -- path taken by enemy
5 -- side length of maze
EESSSESE -- path taken by enemy

Sample Output:
Case #1: ES
Case #2: SEEESSES
"""
tests = int(input())

def solver():
    size = int(input())
    ePath = input()
    
    ePath = ePath.replace("E", "T")
    ePath = ePath.replace("S", "E")
    ePath = ePath.replace("T", "S")
    return ePath

for a in range(tests):
    print("Case #%d: %s" % (a+1, solver() ))
