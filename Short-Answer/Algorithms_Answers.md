#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n) - This while loop is linear, the number of operations it will perform is linear to the information that we give it.


b) O(n * log(n)) - The for loop would run O(n) because the number of operations is linear to what we would provide. The while loop would be running O(log(n)) because it would be doubling while it is less than the given range and incremeting the sum.


c) O(n) - Recursion will always have an O(n) space.

## Exercise II

<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized. -->

Our function minimized damaged would take probably a range of floors in the building and then probably sift through the range for the floor where the eggs will start not to break.
If we take the given range and divide that range in half we can take a look and see if the eggs are still breaking at the middle of our range. From here we can take a look to see if eggs are breaking in the top and bottom half of the range and throw away the range that doesn't have our perfect number right before where the eggs don't break and this would run in O(log(n)) time. 

