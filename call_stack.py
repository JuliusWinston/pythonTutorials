# The Call Stack
#                    Roommate
#          Cousin -> Cousin   -> Cousin           -> Classmate
# Jesse -> Jesse  -> Jesse    -> Jesse   -> Jesse -> Jesse      -> Jesse

# Example 1:
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a() 