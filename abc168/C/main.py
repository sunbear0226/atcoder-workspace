import sys
import math
 
A, B, H, M = [int(i) for i in input().split()]
thetaA = (H + M / 60) * (math.pi / 6)
thetaB = 2 * math.pi * (M / 60)
print(math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(thetaB - thetaA)))