"""
# 
# File          : medium.py
# Created       : 03/11/21 10:05 AM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   : Investigate  the  use  of  args  and  kwargs  to  enable  multiple  inputs  into  a  method
                  which is  our wrapper function
"""


def decorator_passing_arguments(function):
    # decorator function
    def wrapper_accepting_arguments(*args, **kwargs):
        # args and **kwargs collect all positional and keyword arguments and stores them
        # in the args and kwargs variables

        print("The positional arguments are {}".format(args))
        print("The keyword arguments are {}".format(kwargs))
        function(*args)

    return wrapper_accepting_arguments


@decorator_passing_arguments
def fn_with_arg(x, y, z):
    # The arguments will passed to this function that is being decorated at call time
    print("Arguments are {}, {}, {}".format(x, y, z))


@decorator_passing_arguments
def fn_with_keyword_arg():
    # The arguments will passed to this function that is being decorated at call time
    print("Keyword arguments")


fn_with_arg("hi", "hello", "hey")
fn_with_keyword_arg(firstname="Jason", lastname="Stanley")