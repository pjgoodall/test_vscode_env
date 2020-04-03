import os
from my_module import my_variable

print(f"{my_variable}")
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print(user_paths)

print(os.environ['TEST_VAR'])