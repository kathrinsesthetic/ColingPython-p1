container = ["abc", 1, None]

for element in container:
	if not element:
		continue
	
	print(str(element) * 2)


