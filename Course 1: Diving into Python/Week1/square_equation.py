import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

root1 = 0
root2 = 0

D = b ** 2 - 4 * a * c
root1 = (-b + D ** 0.5) / (2 * a)
root2 = (-b - D ** 0.5) / (2 * a)
print(int(root1))
print(int(root2))