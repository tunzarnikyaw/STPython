def draw_line(n):
    for x in range(n):
        print("*", end="")
    print()


print("Welcome...")
draw_line(30)
draw_line(20)
draw_line(10)
draw_line(50)
for i in range(2, 10):
    draw_line(i)
