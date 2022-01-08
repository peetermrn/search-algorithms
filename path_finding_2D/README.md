BFS, greedy and A* all seem to work just fine. Optimal path cost on the 300x300 map is achieved with BFS and A*.

I also made a separate version of A* that allows diagonal movement. 

All programs print out the map with dots representing the path, the number of cells visited while searching, 
the length of the path and the path itself.


results for the 300x300 map:

BFS:
* visited 47276
* path length: 555
* time: 0.328 seconds

greedy:
* visited 4234
* path length: 983
* time: 0.062 seconds

A*
* visited 8842
* path length 555
* time: 0.093 seconds


A* with diagonal movement and different heuristics:
* visited: 14032
* path length: 375
* time: 0.196 seconds

