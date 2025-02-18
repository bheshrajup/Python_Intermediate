#----------functions parameters----------

#positional paramters
def congrats(name,prize=0):
    print(f"Congratulations! {name}. You won {prize} dollars!")

congrats("Achinaru",1000)
# congrats(1000,"Achinaru") #no error because data type is not set in parameter.But meaningless

#keyword paramters
congrats(prize=500,name="Achinaru")
congrats(name="Achinaru",prize=500) #both are same

#combining positional and keyword parameters
congrats("Achinaru",prize=4000)


#variable length parameters (arbitery)
#*args and **kwargs

def show_numbers(*args):
    print(args)

show_numbers()
show_numbers(1)
show_numbers(1,2,3,4,5,6)

def show_info(**kwargs):
    print(kwargs)

show_info()
show_info(name="Bheshraj")
show_info(name="John",age=50,cast="hero")

def show_all(*args,**kwargs):
    print(args)
    print(kwargs)

show_all()
show_all(1)
show_all(1,3,4)
show_all("Hero",name="Bheshraj")

# show_all(name="Bheshraj",hero)#error

