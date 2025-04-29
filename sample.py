#Sample Python Code
"""
This script demonstrates a simple Python program that includes a function to add two numbers,
prints a greeting message, and calculates the sum of two numbers. It also imports necessary
modules for potential future use.
Functions:
----------
- add_numbers(a, b): Adds two numbers and returns the result.
Global Variables:
-----------------
- a: An integer variable initialized to 200.
- b: An integer variable initialized to 300.
Imports:
--------
- BeautifulSoup: Imported from the `bs4` library for HTML/XML parsing (not used in this script).
- os: Provides a way of using operating system-dependent functionality (not used in this script).
Usage:
------
The script prints a greeting message, calculates the sum of two numbers using the `add_numbers`
function, and prints the result.
"""
"""
#import pdb; pdb.set_trace()  # Set a breakpoint here
def add_numbers(a, b):
    print("Adding numbers...")
    print("Added numbers:", a, b)
    return a + b

# Print a greeting
#import pdb; pdb.set_trace()  # Set a breakpoint here
print("Hello, World!")
a = 200
b = 300
#import pdb; pdb.set_trace()  # Set a breakpoint here
# Call the function
result = add_numbers(5, 7)
print("Sandip soni")
print("The sum is:", result)

from bs4 import BeautifulSoup
import os
import requests
res = requests.get("http://api.open-notify.org/astros.json")
print(res.status_code)
import datetime
day = datetime.datetime.now()
print(day.__str__())
print(day.__repr__())


import subprocess
#data = subprocess.run(["dir"], capture_output=True, text=True, shell=True)
#print(data.stdout)
#print(data.stderr)

def max_p(num):
    exp_d = []
    for _ in range(0, len(str(num))):
        exp_d.append(num % 10)
        num = num // 10
    exp_d.sort(reverse=True)
    #exp_d = "".join(map(lambda x: str(x),exp_d))
    exp_d = "".join([str(x) for x in exp_d])
    return int(exp_d)
print(max_p(728818372))
"""

import pytest

@pytest.mark.parametrize("num, num1", [(1,9),(4,6),(5, 5), (3, 7), (2.5, 7.5)]) 
def test_add(num, num1):
    assert num + num1 == 10, "Test failed"
    print("Test passed")
