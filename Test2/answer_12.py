
def report():


	english = int(input("Please enter English Marks: "))
	math = int(input("Please enter Math score: "))
	computers = int(input("Please enter Computer Marks: "))
	physics = int(input("Please enter Physics Marks: "))
	chemistry = int(input("Please enter Chemistry Marks: "))


	total = english + math + computers + physics + chemistry
	average = total / 5
	percentage = (total / 500) * 100


	if percentage  >= 60:
		print(f'You got a Distinctionand got {percentage}% and average of {average}')
	elif percentage >= 50:
		print(f'You got a Merit and got {percentage}% and average of {average}')
	else:
		print(f'You Failed and got {percentage}% and average of {average}')



report()

