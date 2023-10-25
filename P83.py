class ClassA:
    def funcA(self):
        print("This is funcA()")


class ClassB(ClassA):
    pass


objA = ClassA()
objA.funcA()

objB = ClassB()
objB.funcA()    # OK
