"""
# 
# File          : fibonacci.py
# Created       : 02/11/21 10:29 PM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   : Write a Fibonacci sequence generator numbers in the range 1-21 using the __call__ method
#
"""


class Fibonacci:
    """print fibonacci sequence within a range"""

    def __call__(self, start, end):

        a, b, fib, count = 1, 1, start, 1
        print("Fibonacci Series: ", end=" ")
        while 1:
            print(fib, end=" ")
            count += 1
            a = b
            b = fib
            # loop breaks when sum equals to end range
            if fib == end:
                break
            fib = a + b


if __name__ == "__main__":
    fibonacci = Fibonacci()
    fibonacci(1, 21)
