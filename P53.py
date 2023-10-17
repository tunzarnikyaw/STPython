def draw_line(n, symbol="*"):
    for x in range(n):
        print(symbol, end="")
    print()


print("Welcome...")
# draw_line()         # ERROR
draw_line(30)       # OK
draw_line(20, "#")  # OK


# range(40)           # start=0   step=1
# range(1, 11)        # step=1
# range(10, 0, -1)    
