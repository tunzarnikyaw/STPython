def test():
    x = 20  # local variable
    print("This is test(). x is", x)    # 20


def test2():
    global x
    y = x  # global varible
    print("This is test(). x is", x)    # 20


x = 10  # global variable
print("This is main program. x is", x)  # 10
test()
print("This is main program. x is", x)  # 10
test2()
print("This is main program. x is", x)  # 20
