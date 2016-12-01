#!/usr/bin/env python

'''

Program to generating the first n Fibonacci numbers F(n), printing ...
- ... "Buzz" when F(n) is divisible by 3.
- ... "Fizz" when F(n) is divisible by 5.
- ... "BuzzFizz" when F(n) is prime.
- ... the value F(n) otherwise.

'''


__author__   = 'Ryan Watson'
import sys, os, getopt 
from itertools import compress
 
#Methods used ::

'''
Generate Fib sequence using 
Binet's formual. 

Input :: n --> index to calculate fib. seq. [ int ] 
Output :: fib number at n [ int ]
'''
phi = (1 + 5**0.5) / 2
def fib(n):
	return int(round((phi**n - (1-phi)**n) / 5**0.5))


'''
Figure out if number n is divisible by x. 
Simply done by using mod(n,3) == 0

Input :: n --> number from fib. seq.  [ int ]
         x --> number to divide n     [ int ]
'''
def isDiv(n,x):
	if( (n % x) == 0 ): 
		return True 
	return False
	
	
'''
Figure out if number is prime. 
Checks to see is number is only
divisible by 1 itself.

Input :: number from fib. seq.  [ int ]
'''
def isPrime(n):
	if n < 2:
		return False 
	elif n == 2:
		return True
	for x in range(2, n):
		if n % x == 0:
	    		return False
	return True


'''
Calls three functions above to 
check if current integer is 
1) Prime
2) div. by 3
3) div. by 5

Input :: number from fib. seq.  [ int ]
Output :: tuple -> { Num [int], Num%3 [bool], Num%5 [bool], isPrime [bool] }
'''
def checkNumber(n):
        numTuple = ( n, isDiv(n,3), isDiv(n,5), isPrime(n) );
	return numTuple

'''
Print statement based upon given 
conditions (ie. Buzz if div. by 3 ...) 

Input :: tuple -> { Num [int], Num%3 [bool], Num%5 [bool], isPrime [bool] }
'''
def printFib(numTuple):
	if (sum(numTuple[1:]) < 1):
		print numTuple[0]
		return True
	printList = ["Buzz","Fizz","BuzzFizz"]	
	printList = list(compress(printList, numTuple[1:]))
        print ', '.join(printList)
        return True



'''
   MAIN 
'''
def main(argv):
	from optparse import OptionParser
	help_text = """

			Program to generating the first n Fibonacci numbers F(n), printing ...
			- ... "Buzz" when F(n) is divisible by 3.
			- ... "Fizz" when F(n) is divisible by 5.
			- ... "BuzzFizz" when F(n) is prime.
			- ... the value F(n) otherwise.

		    """
	parser = OptionParser(usage=help_text)
	parser.add_option('-n', type="int" ,action='store', dest = "num", help='''Integer used to generate Fib sequence''')
	(opts, args) = parser.parse_args()
	for num in range(1,opts.num+1):
                # generate fib. sequence 
		fibNum = fib(num)
		# check number to see if it matches condition
		numTuple = checkNumber(fibNum)
		# print statement
		printFib(numTuple)

if __name__=="__main__":
	main(sys.argv[1:])
