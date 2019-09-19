import sys
step_number = int(sys.argv[1])

for i in range(0, step_number):
    print(" " * (step_number - i - 1) + "#" * (i+1))