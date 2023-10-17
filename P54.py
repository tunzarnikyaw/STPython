def draw_line(n=40, symbol="*"):
    for x in range(n):
        print(symbol, end="")
    print()


print("Welcome...")
draw_line()                 # OK
draw_line(30)               # OK
draw_line(20, "#")          # OK
# draw_line("#", 20)        # OK
draw_line(symbol="#", n=25) # OK
draw_line(symbol="?")       # OK
# draw_line("?")              # ERROR