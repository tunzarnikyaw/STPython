def seven():
    print("This is seven()")
    return 7


def elven():
    return 11


def twice(n):
    return n * 2


print("Welcome...")
x = seven()
print(x)        # 7
x = elven()
print(x)        # 11
print( seven() )  # 7

x = seven() + elven()
print(x)        # 18

x = twice(10)
print(x)        # 20

x = twice( seven() )
print(x)        # 14

