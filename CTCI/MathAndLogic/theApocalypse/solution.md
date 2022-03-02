# Problem

In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines. If all families abide by this policy-that is, they have to continue to have children until they have one girl, at which point they immediately stop-what will the gender ratio of the new generation be? (Assume the odds of someone having a boy or a girl on any given pregnancy is equal). Solve this out logically and then write a computer simulation of it. 

# Solution

Ok, so it obviously means that there will be more men than women. Why? Because as soon as a woman is born, that couple is out of the "race". 
For example, some couples will have one child, a woman, and stop. So: 
W

Other couples will have a boy, and then, a girl: 
MW

Others will have two boys, and one girl: 
MMW

So, with every couple, we can ensure that at least one girl will be born, but we dont know how many boys will be born. 

But we do know that the odds for either a boy or a girl to be born are 50%

So, if we consider P for population, then we would have: 

W * P * 0.5 

Because half of the couples will have a girl on the first try. 
Then of the remaining 50% of the couples, 50% will have a girl in the second try. So:
(W+M) * P * 0.5 * 0.5 = (W+M) * P * 0.25

And so on an so forth:
Next: 
(W+M+M) * P * 0.125

As we can see, most of the births are of boys. 
For boys, it would be the sum of i=1 to infinity, times i/2^i

Which would approach 1, but not quite. 

Now, we simulate. 



Buuuuuuut, after simulating, we can see that the actual proportion is mostly the same. I tried with 10000 couples, and the proportion stays mostly equal. 