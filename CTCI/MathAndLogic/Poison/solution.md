# Problem

You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which can be used to detect poison. A single drop of poison will turn the test strip positive permanently. You can put any number of drops on a test strip at once and you can reuse a test strip as many times as you'd like (as long as the results are negative). However, you can only run tests once per day and it takes seven days to return a result. How would you figure out the poisoned bottle in as few days as possible?
Follow up: Write code to simulate your approach

# Solution

What occurs to me right away is to overlap some of the bottles for the tests. 
Like, use one strip to test 200 bottles, and use another to test 200 bottles, but overlap 50 bottles in those. That way, if group 1 gets stained, but not group two, then the poison is in the first 150 bottles. If group 2 gets stained, then the poison is in the latest 150 bottles. if both get stained, then the poison is in the middle 50 bottles. 
The problem with this approach is that we would need several rounds of testing, which would take several days. 

The other approach would be to use the advantage of the test taking 7 days to complete. 

Each strip would get 100 bottles in the first day. This would mean that on day 7, one of those 10 strips would get stained. 
Then, on day 2, we could distribute the 100 bottles of each strip in the other stripes, shifting them. 
That way, on day 8, there would be a second strip that gets stained. 
Finally, on day 3, we could shift them again. 
On day 9, we would have, hopefully, 3 stripes. 
The problem arises if after the shift, the poison ends up in the same strip. If this happens once, then on day 8 there would be no second strip staining. Therefore, we could assume that the second digit of the bottle is the same as in the previous day. the problem would be if in day 7, we get one stain, in day 8 we get another, but no stain in day 9. 
To guarantee that we find the bottle, we would have to do another shift. So, in the worst case scenario, we would get the results on day 10. 