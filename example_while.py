from __future__ import division,print_function

trial=int(input("Choose a multiple of 7:"))

while trial%7 !=0 :
	trial=int(input("That has a remainder. Try again! Choose a multiple of 7:"))
