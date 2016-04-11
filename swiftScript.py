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

'''
Figure out if number is divisible by 3. 
Simply done by using mod(n,3) == 0
'''
def isBuzz(n):
	if(n%3 == 0): 
		print "Buzz"
		return True 
	return False
		

'''
Figure out if number is divisible by 5. 
Simply done by using mod(n,5) == 0
'''
def isFizz(n):
	if(n%5 == 0):
		print "Fizz"
		return True
	return False

''' 
Figure out if number is prime. 
Checks to see is number is only
divisible by 1 itself.
'''
def isBuzzFizz(n):
	if n < 2:
		return False 
	elif n == 2:
		print "BuzzFizz" 
		return True
	for x in range(2, n):
		if n % x ==0:
	    		return False
	print "BuzzFizz"
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
	for num in range(1,opts.num):
		if any( (isBuzz(num) , isFizz(num) , isBuzzFizz(num))):
			pass
		else:
			print num 


if __name__=="__main__":
	main(sys.argv[1:])

