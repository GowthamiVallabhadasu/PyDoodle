#cortesy - https://www.w3resource.com/python-exercises/python-basic-exercise-2.php
"""
  Write a Python program to find out what version of Python you are using.

"""
import sys
import platform

print("\nThe current version is ", sys.version, end="\n\n")
print("The version info is ", sys.version_info, end="\n\n")
print("Another way to find version ", platform.python_version())
