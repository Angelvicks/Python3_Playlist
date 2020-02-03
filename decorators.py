#decorators are use to extend the behaviour of a function without editing the function itself
#so if u use the fxn without the decorator it works fine too
# a decorator is a wrapper fxn that is, its a fxn itself, so u create a decorator by creating a fxn

def cough_dec(func):

    def func_wrapper():
        #code before function
        print('*cough*')
        func()
        #code after function
        print('*cough*')

    return func_wrapper()

@cough_dec
def question():
    print(f'can you give me a discount on that?')

@cough_dec
def answer():
    print(f"it's only 50p you cheapskate")

question()
answer()