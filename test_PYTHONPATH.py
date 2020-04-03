import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print(user_paths)

print(os.environ['TEST_VAR'])