import sys
import math
import time

radius = 5.0

if len(sys.argv) > 1:
    radius = float(sys.argv[1])

area = math.pi * math.pow(radius,2)

print("The area of circle with radius", radius, "is:", area)

try:
    time.sleep(3600)
except:
    pass