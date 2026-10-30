def say_hello():
    print('Hello world!')


def greet_in_person(name: str) -> None:
    print(f'Hello {name}!')


def area_of_rectangle(width: int|float, height: int|float) -> int|float:
    return width * height


def check_if_even(number):
    if number % 2 == 0:
        return True
    return False


def many_params(a, b, c=1, *args, **kwargs):
    print('A:', a, 'B:', b, 'C:', c)
    print(args)
    print(kwargs)


# a = 10
# b = 20
# c = 30
# x = []
# y = {}

# def local_visibility():
#     global b, c
#     a = 1
#     b = 2
#     c += 10
#     print('LOCAL a:', a, 'b:', b, 'c:', c)
#     x.append('HELLO')
#     y['name'] = 'Jack'
#     x = []

# local_visibility()
# print('GLOBAL a:', a, 'b:', b, 'c:', c)
# print(x)
# print(y)


# def wrapper(func):
#     print('Starting')
#     func()
#     print('Finishing')
#     say_hello()
#     say_hello()
#     say_hello()


# def say_hello():
#     print('Hello world!')


# wrapper(say_hello)

# import utilities as utils

# utils.say_hello('Jack')

# PI = 123

# from utilities import say_hello, quadruple

# say_hello('Jack')
# print(quadruple(100))



print('Hello')
print('tester_name', __name__)

if __name__ == '__main__':
    print('Bye')