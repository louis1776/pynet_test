#!/usr/bin/env python
from __future__ import print_function
import pdb

def my_func(x, y, z=20):
    return x + y + z

pdb.set_trace()
print()
return_val = my_func(10, 20, 30)
print("Calling with three positional args: {}".format(return_val))

return_val = my_func(x=10, y=20)
print("Calling with two named args: {}".format(return_val))

return_val = my_func(10, z=13, y=20)
print("Calling with one positional and two named args: {}".format(return_val))

return_val = my_func(x="x", y="y", z="z")
print("Calling with three strings: {}".format(return_val))

return_val = my_func(x=["x"], y=["y"], z=["z"])
print("Calling with three lists: {}".format(return_val))
print()
