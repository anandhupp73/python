#function with argumnents
def func(name,age):
    print(name,age)
func('manu',23)
func(23,'manu')
#function with keyword argumnets
def func(name,age):
    print(name,age)
func(name='manu',age=23)
func(age=23,name='manu')
#function with arbitary arguments
def func(*arg):
    print(arg)
func('manu',23)
func(23,'manu',45,'hello')
func()
func(1)
#function with arbitary keyword arguments
def func(**arg):
    print(arg)
func(name='manu',age=23,course='DM')
func(age=23,name='sanu')

