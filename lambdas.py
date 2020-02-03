nums = [1, 2, 3, 4, 5, 6, 7]

def square(n):
    return n * n
#lambda is an inline anonymous function, ie it can be use for a particular fxn  once
lambda n: n * n

print(list(map(square, nums)))