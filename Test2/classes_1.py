class Employee:
	pass


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Kitumetsie'
emp_1.last = 'Mpofu'
emp_1.email = 'Kitumetsie4@gmail.com'
emp_1.pay = 1000000

emp_2.first = 'Sandie'
emp_2.last = 'Sibanda'
emp_2.email = 'sandie4@gmail.com'
emp_2.pay = 2500000


print(emp_1.email)
print(emp_2.email)


#
class Employee:

	def_init_(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '4@gmail.com'

emp_1 = Employee('Kitumetsi', 'Mpofu',  1000000)
emp_2 = Employee('Sandie', 'Sibanda', 2500000 )


print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))