
whole=int(input("Choose a integer less than 7:"))

if whole > 7:
	print(whole,"is larger than 7. You chose badly. I will fix that for you.")
	whole=5
	print(whole,"is smaller than 7. Better choice! Je Je Je.")
elif whole>5:
	print("Cutting it close.")
	whole=3
	print("I chose",whole,"for you instead")
else:
	print("Your number is fine. Move along.")
