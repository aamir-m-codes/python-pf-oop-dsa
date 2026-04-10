"""

Pending...


Recursion is a concept in which a function has the ability to call itself from within the function again and again and again.

Recursion typically needs a base case and a recurring case.

Base case will be what will be the stopping condition.
Recurring case will allow the function to keep calling itself.

This way, a problem is divided into smaller components. Which are easily solved.
"""

def sum(n):
    if n==1:
        return n
    else:
        return n + sum(n-1)
    
print(sum(5))