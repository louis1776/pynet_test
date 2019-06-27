my_list = [10, 20, 30]
def my_func(x, y, z=20):
    return x + y + z

print("Calling with *args: {}".format(my_func(*my_list)))

my_dict = {}
my_dict["x"] = "x"
my_dict["y"] = "y"
my_dict["z"] = "z"
print("Calling with **kwargs: {}".format(my_func(**my_dict)))
