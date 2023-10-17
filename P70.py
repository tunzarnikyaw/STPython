class MyClass:
    data = "Hello"
    another_data = 123

    def show_all(self):
        print(self.data, self.another_data)


print("This is main program")
print( MyClass.data )
print( MyClass.another_data )

obj = MyClass()
obj.show_all()

