import os
import importlib

from pypath_test_module import splitPythonPath

print(f"PYTHONPATH = {splitPythonPath()}")

try:
    print(f"value of 'Test_Var' from `.env`: {os.environ['TEST_VAR']}")
except KeyError:
    print(f"Failed to print os.environ.'TEST_VAR' from `workspaceFolder/.env`")

my_module_name = "my_module"
try:
    importlib.import_module(my_module_name)
    # from my_module import my_variable
    # print(f"{my_variable}")
except Exception:
    print(f"cannot find module named: {my_module_name}")
