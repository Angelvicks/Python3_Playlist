from space.planet import Planet
from space.calc import planet_mass, planet_vol

planet = Planet('Andy', 5000, 4.5, 'The system')

planet_mass = planet_mass(planet.gravity, planet.radius)
planet_vol = planet_vol(planet.radius)

print(f'{planet.name} has  a mass of {planet_mass} and a volume of {planet_vol}')