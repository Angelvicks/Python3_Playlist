from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram) #the empty string acts like a seperator btw the words return after its shuffles

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

#map(function, data)
#print(list (map(jumble, words)))

#comprehension method
print([jumble(word) for word in words])