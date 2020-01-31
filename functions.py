#def greet():
#     print('hello world')
# greet()

def area(radius):
    return 3.142 * radius * radius

def vol(area, length):
    print(area * length)

l = int(input('enter a length:'))
r = int(input('enter a radius: '))

areacalc = area(r)
vol(areacalc, l)