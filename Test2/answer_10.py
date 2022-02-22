

	

def  get_temparature_state():

	a = 0

	while True:
		temperature = int(input('Enter your Temperature:  '))
		z = a =+ 1

		print(f'Z is called')

		if temperature > 100:
			print('It is hot')
		elif temperature >= 60:
			print('It is just right')

		elif temperature >= 1:
			print('Its freezing')
		else:
			break


# get_temparature_state()



a = 12345

print(id(a))