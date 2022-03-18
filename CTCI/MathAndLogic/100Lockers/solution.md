# Problem

There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers. Next, he closes every second locker. Then, on his third pass, he toggles every third locker (closes it if it is open or opens it if it is closed). This process continues for 100 passes, such that on each pass i, the man toggles every ith locker. After his 100th pass in the hallway, in which he toggles only locker 100, how many lockers are open? 

# Solution

Ok, so, we start with all the lockers open. 
Then, the lockers will be toggled everytime we get 1, or any factor of the number of the locker. 
For example, 18, it will be toggled on 1, 2, 3, 6, 9, and 18. 
But, in this case, 3 and 6 cancel each other. 2 and 9, and 1 and 18, so the locker would be closed at the end. 

For a locker to remain open, we would need it to be odd factors. 

This would only happen with squared numbers. 
And the only squared numbers are the squared first 10 numbers. 

that means, the lockers that would remain open would be: 
1, 4, 9, 16, 25, 36, 49, 64, 81, 100