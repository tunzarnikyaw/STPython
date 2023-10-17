def function1():
    print("This is function1()")


def function2():
    print("This is function2()")


def function3():
    pass


def function4():
    function1()
    function2()


print("Hello")
function1()
function2()
function4()
