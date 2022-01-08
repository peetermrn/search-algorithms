My solution is in monte_carlo.py, you can ignore the other files, I made them for testing and stuff.
I have included four positions here, a random one, X to start and X to make first move. I added win percentage with
n = 200 and n = 1000. 

To my surprise the difference between n = 200 and n = 1000 is quite big.


Random position X to move:

    |       |   
    |       |   
    |       |   
    |   X   |   
    |  OOX  |   
    | OXXXO |   
    ---------   
    |0123456|   
    
    
with n = 200:

    move: 0, wins 109, losses 90, draws 1
    win %: 54.5
    
    move: 1, wins 136, losses 59, draws 5
    win %: 68.0
    
    move: 2, wins 124, losses 74, draws 2
    win %: 62.0
    
    move: 3, wins 117, losses 79, draws 4
    win %: 58.5
    
    move: 4, wins 165, losses 31, draws 4
    win %: 82.5
    
    move: 5, wins 104, losses 92, draws 4
    win %: 52.0
    
    move: 6, wins 106, losses 92, draws 2
    win %: 53.0

with n = 1000:

    move: 0, wins 472, losses 509, draws 19
    win %: 47.2
    
    move: 1, wins 659, losses 319, draws 22
    win %: 65.9
    
    move: 2, wins 634, losses 347, draws 19
    win %: 63.4
    
    move: 3, wins 680, losses 308, draws 12
    win %: 68.0
    
    move: 4, wins 778, losses 214, draws 8
    win %: 77.8
    
    move: 5, wins 536, losses 442, draws 22
    win %: 53.6
    
    move: 6, wins 529, losses 451, draws 20
    win %: 52.9
------------------------------------------------------------------------------------------------------------------------
X to make first move:

    |       |
    |       |
    |       |
    |       |
    |       |
    |       |
    ---------
    |0123456|
with n = 200:

    move: 0, wins 103, losses 97, draws 0
    win %: 51.5
    
    move: 1, wins 106, losses 91, draws 3
    win %: 53.0
    
    move: 2, wins 120, losses 79, draws 1
    win %: 60.0
    
    move: 3, wins 124, losses 75, draws 1
    win %: 62.0
    
    move: 4, wins 121, losses 79, draws 0
    win %: 60.5
    
    move: 5, wins 126, losses 71, draws 3
    win %: 63.0
    
    move: 6, wins 104, losses 95, draws 1
    win %: 52.0

with n = 1000:

    move: 0, wins 515, losses 482, draws 3
    win %: 51.5
    
    move: 1, wins 540, losses 455, draws 5
    win %: 54.0
    
    move: 2, wins 594, losses 402, draws 4
    win %: 59.4
    
    move: 3, wins 615, losses 376, draws 9
    win %: 61.5
    
    move: 4, wins 596, losses 402, draws 2
    win %: 59.6
    
    move: 5, wins 554, losses 436, draws 10
    win %: 55.4
    
    move: 6, wins 495, losses 499, draws 6
    win %: 49.5

------------------------------------------------------------------------------------------------------------------------

X to make second move with n = 200:

    |       |
    |       |
    |       |
    |       |
    |       |
    |   O   |
    ---------
    |0123456|
    
with n = 200:

    move: 0, wins 70, losses 130, draws 0
    win %: 35.0
    
    move: 1, wins 87, losses 113, draws 0
    win %: 43.5
    
    move: 2, wins 79, losses 120, draws 1
    win %: 39.5
    
    move: 3, wins 88, losses 112, draws 0
    win %: 44.0
    
    move: 4, wins 79, losses 117, draws 4
    win %: 39.5
    
    move: 5, wins 77, losses 123, draws 0
    win %: 38.5
    
    move: 6, wins 63, losses 136, draws 1
    win %: 31.5

with n = 1000:

    move: 0, wins 343, losses 652, draws 5
    win %: 34.3
    
    move: 1, wins 368, losses 625, draws 7
    win %: 36.8
    
    move: 2, wins 403, losses 587, draws 10
    win %: 40.3
    
    move: 3, wins 417, losses 577, draws 6
    win %: 41.7
    
    move: 4, wins 391, losses 602, draws 7
    win %: 39.1
    
    move: 5, wins 386, losses 612, draws 2
    win %: 38.6
    
    move: 6, wins 331, losses 663, draws 6
    win %: 33.1