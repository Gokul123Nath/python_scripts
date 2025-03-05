import sys

sys.path.append("c:/Users/kgoku/Documents/python_scripts/utility.py")
sys.path.append("c:/Users/kgoku/Documents/python_scripts/run.py")

from utility import abc

obj = abc()

print(obj.factorial(5))