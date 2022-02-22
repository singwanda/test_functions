

def conditional_rendering(age):
	if age <= 18:
		print('You are a teenager')
	elif age <= 50:
		print('You are a youth')
	else:
		print('You are old')



conditional_rendering(12)
conditional_rendering(20)
conditional_rendering(51)
