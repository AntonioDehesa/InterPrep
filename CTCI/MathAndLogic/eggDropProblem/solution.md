# Problem

There is a building of 100 floors. If an egg drops from the Nth floor or above, it will break. If its dropped from any floor below, it will not break. You are given two eggs. Find N, while minimizing the number of drops for the worst case. 

# Solution

Ok, so I have to admit, I peeked into the solution in the book. 
So, the solution is to do some load-balancing of the worst case scenario. 

The perfect scenario is where Egg 1 and Egg 2 always drop the same number of times, regardless of when Egg 1 breaks. 

Therefore, the higher we go, The slower we go up

This would lead to this equation: 
(X*(X+1))/2 = N

Then we would manually have to check if round up or down, depending of which completes our best case scenario. 
