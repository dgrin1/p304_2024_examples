
for i in range(10):
	print(i)
	
import numpy as np
#Can skip around
for i in range(0,10,3):
	print(i)

#you can loop over real numbers
for r in ([1.,3.,5.]):
	print(r)
	
#loop over strings
for textthing in (["cheese","yogurt","kefir"]):
	print(textthing)
	
#np.arange
q=np.arange(0,3,.1)
print(q)	


for r in np.arange(0,3,.1):
	print(r)
	print(q[r])
u=np.linspace(0,10,11)
print(u)


	
	
	
	
	
	