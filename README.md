# Swift Navigation GNSS software test 

## Overview 

Program to generating the first n Fibonacci numbers F(n), printing ...
  * "Buzz" when F(n) is divisible by 3.
  * "Fizz" when F(n) is divisible by 5.
  * "BuzzFizz" when F(n) is prime.
  * the value F(n) otherwise.

## Running script
To run the script first cd into the directory and change the permision of the file to executable
```bash
chmod +x swiftScript.py
```

Next, you can run the script by simply,

```bash 
./swiftScript.py -n 100
```
where n can be any integer value. 

For the help documentation, you can run,

```bash 
./swiftScript.py -h
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
