def test(s):
    try:
        n = int(s)
        return n
    except:
        return 0
    finally:
        def another_function():
            print("another function")

        another_function()


x = test("10")
print(x)
