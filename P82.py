# import count
from count import Count

class Count2(Count):
    def decrease(self):
        self.data -= 1


# a = count.Count()
a = Count2()
print( a.data )     # 0
print( type(a) )    # <class '__main__.Count2'>

a.increase()
a.increase()
a.increase()
print( a.data )     # 3

a.decrease()        # ERROR
print( a.data )     # 2