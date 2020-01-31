# def ninja_into(dictionary):
#     for key,val in dictionary.items():
#         print(f'I am {key} and I am a {val} belt')

def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name: ')
    ninja_belt = input('enter a belt colour: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n)')
    if another == 'y':
        continue

    else:
        break

# ninja_into(ninja_belts)
belt_count(ninja_belts)