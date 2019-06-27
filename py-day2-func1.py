def my_func(x, y, z=20):
    return x + y + z

print()

print("Calling function with all three positional arguments: {}".format(my_func(10, 20, 30)))
print("Calling function with named arguments x, y: {}".format(my_func(x = 30, y = 40)))
print("Calling function with one positional and two named: {}".format(my_func(20, y = 20, z = 80)))
print("Calling function with three strings: {}".format(my_func(x = "x", y = "y", z = "z")))
print("Calling function with three lists: {}".format(my_func([1, 2, 3], [4, 5, 6], [7, 8, 9])))

