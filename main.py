
# def shem1():
#     a = [1, 2, 3, 4]
#     print(a[::-1])
# shem1()

# def shem2():
#     def etc(some_list: list = []):
#         some_list.append(1)
#         return some_list
#
#     print(etc())
#     print(etc())
#     print(etc())

def test(s: object = [1]):
    s.append(1)
    print(s)
    s = [1, 1]


test()
test()
test()
test()
test()
test()

# def test(a = 123):
#     def decor(func):
#         #####
#         def wrapper(*args, **kwargs):
#             result = func(args, kwargs)
#             return result
#         return wrapper
#     return decor
#
# #
# @test(123562)
# def some(*args, **kwargs):
#     print("some")

# some()
#
# class A:
#     some_arg = 1
#     _some_arg2 = 2
#     __some_arg3 = 3
#
# print(A.some_arg)
# print(A._some_arg2)
# print(A._A__some_arg3)
