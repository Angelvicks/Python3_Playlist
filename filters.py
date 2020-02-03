grades= ['A', 'B', 'F', 'C', 'F', 'A', 'D']

def remove_fails(grade):
    return grade != 'F'
#filter(testing_function, grades), testing _function is either true or flase before returning the grades
#print(list(filter(remove_fails, grades)))

# filtered_grades = []
# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)
# print(filtered_grades)

#comprehension method
print([grade for grade in grades if grade != 'F'])