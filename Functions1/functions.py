def hello_world():
    print("hello world!")

hello_world()

def sum(num1=0, num2=0):
   if (type(num1) is not int or type(num2) is not int ):
        return
   return num1 + num2

total = sum()
print(total)




def multiple_items(*args): #Cant do anything wih the variables outside of this
    print(args)
    print(type(args))

multiple_items("Dave","John","Sara")


def mult_named_items(**kwargs): #usues keywords so the things in it can be reffered to
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last ="gray")