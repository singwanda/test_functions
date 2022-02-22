

def get_datatypes(x, y, z):

	string = x

	integer = y

	boolean = z

	types = [type(x), type(y), type(z)]

	print(f"{string} is string")
	print(f"{integer} is integer")
	print(f"{boolean} is boolean")

	return types



print(get_datatypes('Mphilisi', 12, True))