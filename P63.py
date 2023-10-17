try:
    a = input("Enter a number: ")
    b = input("Enter a number: ")
    c = int(a) / int(b)
    print("The result is", c)
except ValueError:
    print("Please enter number only")
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Unknown error!")
else:
    print("Executed")
finally:
    print("Finally")
