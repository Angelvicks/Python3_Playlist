from classes import Planet

planet = Planet('Andy', 5000, 4.5, 'The system')
print(f'Name is: {planet.name}')
print(f'Radius is: {planet.radius}')
print(f'The gravity is: {planet.gravity}')
print(planet.spin('at a very high speed'))
print(Planet.spin())

#Packages are a collection of modules