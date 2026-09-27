"""
Module 2 — Lesson 3: Loops & Lists
Student: Anunciacion John Lheiywin Clever V.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Imagine a list as an organized shopping list on paper—it lets you group multiple 
items together under a single name instead of creating a separate variable for 
every single item. 

Loops are your way of automating repetitive tasks. Instead of copying and pasting 
the same code 100 times to process each item on your list, a loop lets you say: 
"Take this list, go through it item by item, and do this action for every single 
one until you reach the end." It saves time, eliminates human error, and handles 
massive amounts of data effortlessly.


============================================
KEY VOCABULARY
============================================
- list: An ordered, changeable collection of items enclosed in square brackets `[]` 
  that can hold multiple values of any data type.
- for loop: A loop used to iterate over a sequence (like a list, string, or range) 
  a specific number of times or once for each item in the sequence.
- while loop: A loop that continues executing a block of code repeatedly as long as 
  a specified condition remains True.
- index: The numerical position of an item inside a list, starting at 0 for the first 
  item (e.g., `my_list[0]` accesses the first item).
- iteration: One single pass or cycle through a loop.
- append(): A list method used to add a new item to the very end of an existing list.


============================================
MY OWN EXAMPLE(S)
============================================
"""


quiz_scores = [88, 92, 65, 74, 98, 100, 58, 81]

total_score = 0
honor_roll_scores = []

print("=== PROCESSING QUIZ SCORES ===")

for score in quiz_scores:
    total_score += score  # Accumulate sum for average calculation
 
    if score >= 90:
        honor_roll_scores.append(score)

average_score = total_score / len(quiz_scores)

print(f"Total Students: {len(quiz_scores)}")
print(f"Class Average: {average_score:.1f}")
print(f"Honor Roll Scores (90+): {honor_roll_scores}")

countdown = 3
print("\n--- Posting Final Ranks ---")
while countdown > 0:
    print(f"Publishing in {countdown}...")
    countdown -= 1  # Decrement counter to prevent an infinite loop

print("Results successfully published!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Two classic mistakes tripped me up while learning loops and lists:

1. Off-by-One / Zero-Based Indexing Errors:
   Remembering that lists start at index `0` instead of `1` took practice! 
   If a list has 5 items, the last item is at index `4`. Trying to access 
   `my_list[5]` triggers an `IndexError: list index out of range`.

2. Creating an Infinite While Loop:
   When writing a `while` loop, you must ensure the variable controlling the loop 
   condition changes inside the loop body (like `countdown -= 1`). If you forget to 
   update it, the condition stays `True` forever, crashing or freezing your program!


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Loops and lists are the backbone of batch processing in web applications, automated 
testing, and data analysis. 

For example, when an e-commerce platform like Amazon generates your digital receipt, 
it uses a list of items in your cart. A `for` loop iterates through each item to sum 
the prices, apply individual item taxes, calculate shipping fees, and generate a line 
item on your bill automatically—regardless of whether you bought 1 item or 100.
"""