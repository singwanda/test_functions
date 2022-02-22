





#previous test qstns into func :average





	



#

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











