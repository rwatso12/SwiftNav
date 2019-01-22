# Python Implementation of FizzBuzz 

## Overview 

Program to generating the first n Fibonacci numbers F(n), printing ...
  * "Buzz" when F(n) is divisible by 3.
  * "Fizz" when F(n) is divisible by 5.
  * "BuzzFizz" when F(n) is prime.
  * the value F(n) otherwise.

## Running the script
To run the script first cd into the directory and change the permision of the file to executable
```bash
chmod +x fizz_buzz.py
```

Next, you can run the script by simply,

```bash 
./fizz_buzz.py -n 100
```
where n can be any integer value. 

For the help documentation, you can run,

```bash 
./fizz_buzz.py -h
```
which will pop up as 

```bash
Usage: 

			Program to generating the first n Fibonacci numbers F(n), printing ...
			- ... "Buzz" when F(n) is divisible by 3.
			- ... "Fizz" when F(n) is divisible by 5.
			- ... "BuzzFizz" when F(n) is prime.
			- ... the value F(n) otherwise.

		    

Options:
  -h, --help  show this help message and exit
  -n NUM      Integer used to generate Fib sequence
  ```
