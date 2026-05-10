"""
Recursion is a concept in which a function has the ability to call itself from within the function again and again and again.

Recursion typically needs a base case and a recurring case.

Base case will be what will be the stopping condition.
Recurring case will allow the function to keep calling itself.

This way, a problem is divided into smaller components. Which are easily solved.
"""

def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
    
print(sum(5))

"""
in the above example. the constant 5 is passed to the recursive functiom.

in first case, it will return:
5 + sum(4)

in next case, it will return:
4 + sum(3)

then 
3 + sum(2)
2 + sum(1)

this way it will stop at base case, where it will return 1.


5 + sum(4)
sum(4) is '4 + sum(3)'
sum(3) is '3 + sum(2)'
sum(2) is '2 + sum(1)'
sum(1) is 1

so at end:

5 + 4 + 3 + 2 1

"""
