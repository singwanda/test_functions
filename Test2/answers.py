
def hello():
	name = str(input("Enter your name: "))
	if name:
		print("Hello " + str(name))

	else:
		print("Hello world")

	return 


hello()
#
is_hot = False

if is_hot:
	print('eyy boss it is very difficult to be a man, there are too much obstacles that you meet in life')
	print('wear your sunhats its a hot day')

else:
	print('enjoy your day')


#
price = 1000000
has_good_credit = False

if has_good_credit:
	down_payment = 0.1 * price
else:
	down_payment = 0.20 * price

print(down_payment)

#
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
	print('Eligible for loan')

else:
	print('awotholi nex wena kkkkk')


#
temp = 35
if temp > 30:
	print("it is a hot day")
else:
	print("it is a not a hot day")


#
cordinates = (1, 2, 3)
x, y, z = cordinates

print(y)