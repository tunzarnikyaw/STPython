def test():
    print("This is test()", x)


# test()  # ERROR
# print("This is main program", x)  # ERROR
x = 10
print("This is main program", x)
test()      # OK

