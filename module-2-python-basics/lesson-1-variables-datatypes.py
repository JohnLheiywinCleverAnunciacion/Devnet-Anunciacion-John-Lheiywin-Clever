"""
Module 2 — Lesson 1: Variables & Data Types
Student: Anunciacion John Lheiywin Clever V.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Think of a variable as a labeled storage box inside your computer's memory. 
When you write code, you create a box, put a label on it (the variable name), 
and put something inside it (the value). Whenever you want to use or change 
what's inside that box later, you just call it by its label.

A "data type" is simply the kind of thing you decide to store inside that box. 
Computers need to know if you are giving them a whole number, a decimal, a piece 
of text, or a simple true/false answer so they know how to handle it properly. 
For example, you can do math with numbers, but you can't subtract a word from another word!


============================================
KEY VOCABULARY
============================================
- variable: A named container used to store data values in memory that can be referenced 
  and updated later in your code.
- data type: A classification that tells the computer what kind of value a variable holds 
  (e.g., text, number, true/false) and what operations can be performed on it.
- int (integer): A data type representing whole numbers without decimals (positive, 
  negative, or zero, e.g., 42, -5, 0).
- float (floating-point number): A data type representing real numbers that contain 
  a decimal point (e.g., 3.14, 99.99, -0.5).
- string (str): A sequence of characters wrapped in single or double quotes used to 
  represent text (e.g., "Hello World", 'Lheiywin').
- boolean (bool): A data type that can only have one of two values: True or False.
- type casting: The process of manually converting a value from one data type to 
  another (e.g., converting the string "5" into the integer 5 using int("5")).


============================================
MY OWN EXAMPLE(S)
============================================
"""

player_name = "ShadowKnight"   # string (str)
level = 15                    # integer (int)
health_points = 87.5          # float
has_magic_key = True          # boolean (bool)


print("=== PLAYER STATUS ===")
print("Player Name:", player_name)
print("Current Level:", level)
print("Health Points:", health_points)
print("Has Key:", has_magic_key)

level += 1                    # Increase level by 1
health_points -= 12.3         # Take damage
has_magic_key = False         # Used the key on a door

print("\n--- Data Types Check ---")
print("player_name type:", type(player_name))
print("level type:", type(level))
print("health_points type:", type(health_points))
print("has_magic_key type:", type(has_magic_key))


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
A common mistake is trying to concatenate (join) a string with a number directly, 
like this: `print("Your total score is " + score)`. In Python, this throws a `TypeError` 
because Python won't automatically combine text with numbers. 

To avoid this error, you either have to convert the number to a string using `str(score)`, 
use commas inside the print statement `print("Your total score is", score)`, or use an 
f-string like `print(f"Your total score is {score}")`.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Variables and data types are the foundation of every app or digital system we use daily. 
For example, when you check your digital bank account, your balance is stored as a float 
(e.g., 1250.50), your account holder name is a string ("Alex Rivera"), your transaction count 
is an integer (12), and whether your card is active or locked is a boolean (True/False). 
Without data types, software wouldn't know how to handle financial calculations versus 
displaying text on a screen.
"""