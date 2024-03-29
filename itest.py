from __future__ import print_function,division
import numpy as np
N=1000
a=0
b=2

ivec=range(0,N+1)
s=0
x=0
h=float(b-a)/float(N)

def f(x):
	f=x**2.
	return f


for i in ivec:
	s+=f(x)*h
	x=a+i*h

def trape(a,b,f,N):
	h=(b-a)/N
	s=(f(a)+f(b))*h
	for i in range(1,N):
		s+=2.*f(a+i*h)*h
	s/=2.0
	return s
	
trape(a,b,f,N)

print(s,trape(a,b,f,N))
from gaussxw import gaussxwab
x,w=gaussxwab(3,0,2)
integ_gauss=sum(f(x)*w)
print(integ_gauss)
from scipy.integrate import fixed_quad
integ_scipy=fixed_quad(f,a,b)
print(integ_scipy[0])
from scipy.integrate import romberg
integ_rom=romberg(f,a,b)
print(integ_rom)
