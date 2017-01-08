#!/usr/bin/env python

'''
Program to generating the first n Fibonacci numbers F(n), printing ...
- ... "Buzz" when F(n) is divisible by 3.
- ... "Fizz" when F(n) is divisible by 5.
- ... "BuzzFizz" when F(n) is prime.
- ... the value F(n) otherwise.


How to Run ??
    ./fizz_buzz.py -n 5
'''


__author__ = 'Ryan Watson'

from itertools import compress

FIB_CONST = (1 + 5**0.5) / 2

def fib(num):

    '''
    Generate the nth number of the Fib sequence using
    Binet's formual.
    Input :: n --> index to calculate fib. seq. [ int ]
    Output :: fib number at n [ int ]
    '''

    return int(round((FIB_CONST**num - (1-FIB_CONST)**num) / 5**0.5))


def is_div(num, div):

    '''
    Figure out if number num is divisible by div.
    Simply done by using mod(num,div) == 0
    Input :: num --> number from fib. seq.  [ int ]
             div --> number to divide num     [ int ]
    '''

    if num%div == 0:
        return True
    return False


def is_prime(num):

    '''
    Figure out if number is prime.
    Checks to see is number is only
    divisible by 1 itself.
    Input :: num from fib. seq.  [ int ]
    '''

    if num < 2:
        return False
    elif num == 2:
        return True
    for div in xrange(2, num):
        if num % div == 0:
            return False
    return True


def check_number(num):

    '''
    Calls three functions above to
    check if current integer is
    1) Prime
    2) div. by 3
    3) div. by 5
    Input :: number from fib. seq.  [ int ]
    Output :: tuple -> { Num [int], Num%3 [bool], Num%5 [bool], isPrime [bool] }
    '''

    num_tuple = (num, is_div(num, 3), is_div(num, 5), is_prime(num))
    return num_tuple


def print_fib(num_tuple):

    '''
    Print statement based upon given
    conditions (ie. Buzz if div. by 3 ...)
    Input :: tuple -> { Num [int], Num%3 [bool], Num%5 [bool], isPrime [bool] }
    '''

    if sum(num_tuple[1:]) < 1:
        print num_tuple[0]
        return True
    print_list = ["Buzz", "Fizz", "BuzzFizz"]
    print_list = list(compress(print_list, num_tuple[1:]))
    print ', '.join(print_list)
    return True


def main():

    '''
    Program to generating the first n Fibonacci numbers F(n), printing ...
    - ... "Buzz" when F(n) is divisible by 3.
    - ... "Fizz" when F(n) is divisible by 5.
    - ... "BuzzFizz" when F(n) is prime.
    - ... the value F(n) otherwise.
    '''

    from optparse import OptionParser
    help_text = """
			Program to generating the first n Fibonacci numbers F(n), printing ...
			- ... "Buzz" when F(n) is divisible by 3.
			- ... "Fizz" when F(n) is divisible by 5.
			- ... "BuzzFizz" when F(n) is prime.
			- ... the value F(n) otherwise.
		    """
    parser = OptionParser(usage=help_text)
    parser.add_option('-n', type="int", action='store', dest="num",
                      help='''Integer used to generate Fib sequence''')
    opts, _ = parser.parse_args()
    for num in xrange(1, opts.num+1):
        # generate fib. sequence
        fib_num = fib(num)
        # check number to see if it matches condition
        num_tuple = check_number(fib_num)
        # print statement
        print_fib(num_tuple)


if __name__ == "__main__":
    main()
