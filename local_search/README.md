Solution works fine on boards of size 10 and smaller but bigger boards take quite some time.

I find the best move by by checking all the moves all the queens can make.

I found a situation where the way I find the best move kinda breaks down.
That happens when queens are in a straight line:

1111  
0000  
0000  
0000  

or

1000  
0100  
0010  
0001  


This doesn't work because by moving only one queen you always have the same amount or more conflicts.

To combat this I added some code so that when the best move doesnt have less conflicts I check if the
solution can be found at all (if the amount of queens on board is less or equal to board size).
If it can be found then I reshuffle the board and start over.

Made some helper methods (nxn_queens_random and nxn_queens_diagonal) to display boards and solutions. 
