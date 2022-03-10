print("========================================================================")
# "pip install name_of_library" will download and install the library

print("1--------------------------------")
import mymodule 

mymodule.my_func()

print("2--------------------------------")
import mymodule as mm

mm.my_func()

print("3--------------------------------")
from mymodule import my_func, my_func2

my_func()
#my_func1()		# this one is not imported
my_func2()


print("========================================================================")