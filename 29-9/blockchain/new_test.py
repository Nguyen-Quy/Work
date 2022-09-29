import hashlib
import json
from time import time
from tkinter import Y
from uuid import uuid4

# 22 % /m * 15y
# -> 45 % /m + 2 % /Y

# 2200000 * 12 * 15
# 4500000
x = 1
y = 0
while hashlib.sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
print(f'The solution is y ={y}')
