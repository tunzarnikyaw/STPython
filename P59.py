def test():
    y = 20  # local variable
    print("This is test(). x is", x)    # OK x is global
    print("This is test(). y is", y)    # OK y is local to test()


def test2():
    print("This is test2(). x is", x)   # OK x is global
    # print("This is test2(). y is", y)   # ERROR y is local to test()


x = 10  # global variable
print("This is main program. x is", x)
test()
test2()
