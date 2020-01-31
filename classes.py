class Planet:
    #class level instant variable, attributes
    shape = round

# Init function is required when we create a new class and it takes the self parameter when u create a new instance as in self.name
# Self is mostly important for initialisation of the new objects in the class that makes it easy to then create properties or attributes of the class later
  #intant attributes
    def __init__(self, name, radius, gravity, system): #the variable inside def is to accept then in the intialisation function
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
# we have instant attributes and instant methods meaning they are unique to the instance
#instant methods
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    #its a method doesnt have access to self and the class itself as well as the class level attributes, it has access to the parameters passed individually to it
    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'All planets spins and spins at {speed}'
#hoth and planet are individual instances where u create a new Planet for the class, the can also access class level intances
# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System' )
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'The gravity is: {hoth.gravity}')
# print(hoth.orbit())

planet = Planet('Andy', 5000, 4.5, 'The system')
# print(f'Name is: {planet.name}')
# print(f'Radius is: {planet.radius}')
# print(f'The gravity is: {planet.gravity}')
# print(planet.orbit())

# print(Planet.shape)
# the classmethod common is access from the class and also from the instances of the class like planet or hoth
print(Planet.commons())
print(planet.commons())

#The class can't access instance method on itself i.e print(Planet.orbit()) will give error

print(Planet.spin())
print(planet.spin('at a very high speed'))