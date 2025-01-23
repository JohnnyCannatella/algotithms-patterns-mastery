# Two Pointers Pattern

## Pattern Description
- two pointer algorithm has these characteristics:
  - Two moving pointers, regardless of directions, moving dependently or independently; 
  - A function that utilizes the entries referenced by the two pointers, which relates to the answer in a way;
  - An easy way of deciding which pointer to move; 
  - A way to process the array when the pointers are moved.
- **Common Uses**: 
  - It’s commonly applied to problems involving pairs, 
    • such as pair sums, 
    • palindrome checking, 
  - or scenarios where you need to compare elements from opposite ends of a sequence.
- 
- classification:
  - **Same direction:** 
    - the function used in this question is comparing the value of the fast pointer to its previous entry and see if they match
      - Typically used for cycle:
        - Fast always advances by one
        - For loop automatically handles this movement
        - Slow moves conditionally
  - **Opposite direction:**
    - the function is comparing the sum of the entries to the desired amount. If the sum is greater, we move the larger pointer, 
    - and if the sum is lesser, we move the smaller pointer. If the sum is equal, we find our answer, and we stop the program.
      - Both pointers move conditionally
      - While allows more control over when to move them
      - We need to check that they do not cross
  - Fast and Slow
    - Specifico per problemi nelle linked list
  - **Sliding window:**
    - we keep track of the number of characters that appear in the window. We move the later pointer, inserting the item into the set, 
    - until there is a duplicate. Then, we move the earlier pointer, removing items out of the set, until we can insert the item. We also keep track of the largest size each time for the answer.
- Note:
  - The two-pointer technique is not limited to arrays. Two pointer can be done on other structures, like linked list, as long as they are iterable.
  - Two pointers are helpful because it often offers a more efficient solution than the naive solution. (less complexity)

- **Common Uses**:
  **You have an ORDERED array, and you need to find a pair of elements that satisfy a condition**
  Example: “find two numbers that sum to X”
  Why it works: sorting allows you to move pointers around intelligently
  
  **You have to compare elements from “opposite ends”**
  Example: “check if it is palindrome”
  Why it works: you can compare start and end simultaneously
  
  **You need to find a “meeting point” or “window”**
  Example: “find the container with the most water”
  Why it works: you can narrow the search space on both sides
  
  **You work with duplicate elements in an ordered array**
  Example: “remove duplicates in-place”
  Why it works: one pointer keeps track of the “clean” position, the other explores
  
  **You need to find a loop in a linear structure**
  Example: “find loop in linked list”
  Why it works: slow and fast pointer will meet in the loop

