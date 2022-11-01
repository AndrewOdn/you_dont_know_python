""" What will be on the screen after the function is executed? """
def func1():
    a = [1, 2, 3, 4]
    print(a[::-1])


func1()


def func2(s: object = [1]):
    s.append(1)
    print(s)
    s = [1, 1]


func2()
func2()
func2()
