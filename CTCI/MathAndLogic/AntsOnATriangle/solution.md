# Problem

There are 3 ants on different vertices of a triangle. What is the probability of collision (between any two or all of them) if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen, and that they walk at the same speed. 

Similarly, find the probability of collision witn n ants on an n-vertex polygon. 

# Solution

Ok.
In the case of the triangle, the possibility for going left or right would be 50% or 1/2.  
And the probability of collision would be:
P() = A1 and A2, or A2 and A3, or A1 and A3.
And for A1 and A2 to collide, it would require A1 to go left, and A2 to go right.
So, it would really be:
P() = A1Left and A2Right, or A2Left and A3Right, or A1Right and A3Left.
Which would be translated as:
P() = 1/2 * 1/2 + 1/2*1/2 + 1/2*1/2
which would be:
P() = 3/4 = 0.75

We can generalize by saying:
P(Left) = 1/2 ^3
P(Right) = 1/2 ^3
P(All in the same direction) = P(Left) + P(Right) = 1/4

But it is 3 because it is 3 ants in a triangle.
For a n-side polygon, we just substitute 3 for n. and done
