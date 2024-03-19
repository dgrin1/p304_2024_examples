from __future__ import print_function,division
import numpy as np


"SIMPSON RULE"

N=10 #slices
a= float(input("What is a? "))#lower integration #i did a=0
b=float(input("What is b? ")) #upper #b=2
 
ivec=range(0,N+1)
s=0
x=0

#step size
h=float(b-a)/float(N)


def f(x): #define function
	f=x**2. #f= x^2
	return f
	
	
for k in ivec:#adding area of rectangle
	s+=f(x)*h
	x=a+k*h

def simp(a,b,f,N): #simpson rule
	h=(b-a)/N  #stp size
	s=(f(a)+f(b)*h)
	for k in range(1,N,2):#odd numbers of N-1
		s+=4.*f(a+k*h)*h #+4(f(a+kh))
		for k in range(2,N-1,2):
			s+=2.*f(a+k*h)*h #+2(f(a+kh))
	s/=3.0 #h/3
	return s

print(simp(a,b,f,N))