fruits = ["Apple", "Orange", "Mango"]
# x = [123, "test", 3.5, True]

print(fruits)   # ["Apple", "Orange", "Mango"]

fruits.append("Banana")

print(fruits)   # ["Apple", "Orange", "Mango", "Banana"]

fruits.insert(2, "Grape")

print(fruits)   # ["Apple", "Orange", "Grape", "Mango", "Banana"]

fruits.remove("Apple")

print(fruits)   # ['Orange', 'Grape', 'Mango', 'Banana']

fruits[0] = "Coconut"

print(fruits)
