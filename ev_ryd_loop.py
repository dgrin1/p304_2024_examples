#### Code to ask user energy level, and output floating poitn values
#n=input("What energy level of H would you like?")
#n=int(n)

n=0
m=0
while(n<100):
	n+=1
	m=0
	while(m<100):
		m+=1
		energy=-(13.6/n**2-13.6/m**2)
		print("The energy of this level is ", energy)