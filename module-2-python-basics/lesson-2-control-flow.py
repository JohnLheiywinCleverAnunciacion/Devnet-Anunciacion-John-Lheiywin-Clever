"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Anunciacion John Lheiywin Clever V.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is how a program makes decisions and decides which path to follow. 
Normally, code runs line-by-line from top to bottom. Control flow lets you tell 
the computer: "If option A is true, do this. If not, check option B. Otherwise, 
do option C."

It works just like real-life choices. For example: IF it's raining, bring an umbrella. 
ELSE IF (elif) it's overcast, bring a light jacket. ELSE (if neither is true), wear 
sunglasses. It gives your program a brain to react differently depending on the situation!


============================================
KEY VOCABULARY
============================================
- condition: A statement or expression that evaluates to either True or False, 
  determining whether a block of code should run.
- if / elif / else: The core keywords used for decision-making in Python:
    - 'if' tests the first condition.
    - 'elif' (short for else if) tests additional conditions if previous ones were False.
    - 'else' acts as a catch-all block that runs if none of the above conditions were True.
- comparison operator: Symbols used to compare two values, such as `==` (equal to), 
  `!=` (not equal to), `>` (greater than), `<` (less than), `>=` (greater or equal), 
  and `<=` (less or equal).
- boolean expression: Any code snippet that evaluates to a Boolean value (`True` or `False`), 
  such as `age >= 18`.
- logical operators: Keywords like `and`, `or`, and `not` used to combine multiple 
  conditions together into a single decision.


============================================
MY OWN EXAMPLE(S)
============================================
"""


customer_age = 16
is_student = True
is_matinee = False  # Matinee showtimes get a discount regardless of age

print(f"Customer Details: Age {customer_age}, Student: {is_student}, Matinee: {is_matinee}")


if is_matinee:
    ticket_price = 8.00
    ticket_type = "Matinee Special"
elif customer_age < 12:
    ticket_price = 7.50
    ticket_type = "Child"
elif customer_age >= 65:
    ticket_price = 9.00
    ticket_type = "Senior"
elif is_student and customer_age <= 22:
    ticket_price = 10.00
    ticket_type = "Student Discount"
else:
    ticket_price = 14.00
    ticket_type = "Standard Adult"

print(f"Ticket Type: {ticket_type}")
print(f"Total Amount Due: ${ticket_price:.2f}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Two major mistakes tripped me up when learning control flow:

1. Confusing `=` with `==`: 
   Using a single equal sign `=` assigns a value to a variable, whereas a double 
   equal sign `==` checks if two values are equal. Writing `if score = 100:` causes 
   a `SyntaxError`.

2. The order of conditions matters:
   Python evaluates `if` and `elif` blocks from top to bottom and stops as soon as it 
   finds the FIRST `True` condition. If I checked `elif customer_age >= 18` before checking 
   `elif customer_age >= 65`, seniors would get matched with the adult price first and 
   never reach their discount condition!


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Control flow is the core foundation of user authorization and security logic in modern 
software. When you log into an app, control flow checks:
- IF the password matches AND 2FA is verified -> Grant access.
- ELIF the password matches BUT 2FA fails -> Prompt for backup code.
- ELIF account is locked after 5 bad attempts -> Show lockout screen.
- ELSE -> Display "Invalid Username or Password".
"""