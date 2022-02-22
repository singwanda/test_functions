#question1
def plus(a,b):
	return a + b 

a = 2020
b = 10

print(plus(a,b))

#question 2
def hello_function():
		 print('Hello world, it is my day. Function.')

hello_function()

#
def greet():
	print("Hello")
	print("How do you do")

greet()

 

#question3 :args 
def myWorld(*zim):
    for arg in zim:
    	print(arg)

myWorld('Hello', 'welcome', 'to', 'Zimbabwe')

#**kwargs 
def myWorld(**kwargs):
   for key, value in kwargs.items():
       print("%s == %s" %(key, value))

myWorld(first ='Zim', mid ='for', last ='Zimbos')


#question 4
def my_str():
	return my_str

new = ['p','q','r']
my_str = 'there are too much person a, person b, person c.'
old = ['a','b','c']

for i in range(0,len(old)):
	my_str = str.replace(my_str,old[i],new[i])

print(my_str) 


#question5
def my_vowels():
	return my_vowels

my_vowels = ['e','o','a','i','u']
my_vowels.sort()

print('sorted list:', my_vowels)


#previous test qstns into func :average

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
	
#
def pop_list(x):
	

	return x.pop()


def index_list():
	

	return x[0]



def append_list(x):
	
	y = 'max'

	full_list = x.append(y)

	return full_list



def sort_list(x):
	
	x.sort()

	return x


def join_list(x):
	

	return '-----'.join(x)




x = ['Mabidza', 'Nkosi', 'Mphilisi']



print(join_list(x))

#


def pop_list(x):
	

	return x.pop()


def index_list(x):
	

	return x[0]



def append_list(x):
	
	y = 'max'

	full_list = x.append(y)

	return full_list



def sort_list(x):
	
	x.sort()

	return x


def join_list(x):
	

	return '-----'.join(x)




x = ['Mabidza', 'Nkosi', 'Mphilisi']



print(join_list(x))



#
def x():
 	 print("Remote sensing")
 	 print("mphilisi mpofu")
	
	
x()

def is_raining():
	print("it's a wet day")
	print("take out your umbrella")


is_raining()

def is_sunny():
	print("it's a sunny day")
	print("wear your sun hats")


is_sunny()

#
def weight_lbs(): 
	weight_lbs = input('weight (lbs): ')
	weight_kg = int(weight_lbs) * 0.45


print(weight_lbs)

#  
def unlock(password):
	return password 

password = ("BARIDZI", "MPHILISI", "ALMS")

password = input('May you enter your password')

if password == ("BARIDZI", "MPHILISI", "ALMS"):

	print("Welcome to desert of the real")


else:
	print("No")

	print("Sorry only Mphilisi, Alms and Baridzi are allowed to view this content")


print(unlock(password))

#
def valuable(minerals):
	return minerals

minerals = ["gold","silver","diamond","aliminium","cobalt","copper"]



for mineral in minerals:
	if mineral != "cobalt":
		print(mineral.upper())
	else:
		print(mineral)



valuable(minerals)


 #qstn5 create a dictionary with student names as key values as a subject
def marklist(data):
	return data

data = {'John': [{'subject1': "maths",'marks': 95},
                  {'subject2': "english",'marks': 80}],
         'Peter': [{'subject1': "maths",'marks': 70},
                   {'subject2': "english",'marks': 60}]}



for key, values in data.items():
     for i in values:
     	print(key, " : ", i)




marklist = dict()



mphi = marklist["Mphilisi"] = 20
mphi = marklist["Alms"] = 20
mphi = marklist["Bheki"] = 20
mphi = marklist["Max"] = 20



for key in marklist:
  print(key)




for value in marklist.values():
  print(value)

for key in marklist.keys():
  print(key)




for key, value in marklist.items():
  print(key, value)





print(marklist["Mphilisi"])
print(marklist["Max"])

# statements
def statement(a):
	return a
a = 10
while a <= 20:
 print(a)
 a = a + 10
print("Done")

statement(a)


#
def true(temperature):
	return temperature

temperature = int(input('Enter your temperature>>> '))

if temperature > 100:
	print("It is hot")
elif temperature >= 60:
	print('It is warm')
elif temperature >=  1:
	print('It is cold')


#
#qstn11
def report(total):
	return total

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



print(report(total))











