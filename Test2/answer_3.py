

#question3 :args 
def myWorld(*zim):
    for arg in zim:
    	print(arg)



# myWorld(1, 2, 4)



def args_and_kwargs(att, *args, **kwargs):
	print(f'ARGS: {args}')
	print(f'KWARGS: {kwargs}')
	print(f'ATT: {att}')




args_and_kwargs('Mpofu', 'Moyo', 0, s = 'Tshuma', name='Baridzi', mark=30, )




def get_fullname(name, surname):

	print(name)
	print(surname)



get_fullname(surname='Mpofu', name='Mphilisi')



def myWorld(**kwargs):
   for key, value in kwargs.items():
       print(f"{key}= {value}" )

myWorld(first ='Zim', mid ='for', last ='Zimbos')
