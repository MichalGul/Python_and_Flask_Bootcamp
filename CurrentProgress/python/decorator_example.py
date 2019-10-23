


def hello(name="Jose"):
    print('the hello() func has been run')

    def greet():
        return "     This is inside the greet()"


    def welcome():
        return "     This is inside welcome()"

    if name=="Jose":
        return greet
    else:
        return welcome

#a = hello()
#print(a())



#----------------#
def hello2():
    return "Hi Jose"

def other(func):
    print("Some other code")
    # Assumed that func is function
    if callable(func):
        print(func())

#other(hello2)
#---------------------# Decorator building

def new_decorator(func):

    def wrap_func():
        print("some code before execution func")

        func()

        print("Code here, after executing func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Please decorate me!!")


# func_needs_decorator()
# #Brzydkie uderokorowanie funkcji, gdy nie ma malpy (dekoracji) przed fuinkcja
# func_decorated = new_decorator(func_needs_decorator)
# func_decorated()
func_needs_decorator()