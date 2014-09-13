#!/usr/bin/python

import sys

# Defines a repeat function that takes 2 arguments
# It repeats the first argument 3 times and if the second argument exists it adds !!! to the end result

def repeat(s, exclaim):
	result = s*3
	if exclaim:
		result = result + "!!!"
	return result

def main():
	if len(sys.argv) >= 3:
		valor = repeat(sys.argv[1],sys.argv[2])
		print valor
	else:
		print "Please provide two arguments"
	

# Standard boilerplate

if __name__ == "__main__":
	main()
