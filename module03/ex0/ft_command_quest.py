import sys

print("=== Command Quest ===")
length = len(sys.argv)
index = 1
if length == 1:
    print("No arguments provided!")

print("Program name: ", sys.argv[0])
if length != 1:
    print("Arguments received:", length-1)
    for arg in sys.argv[1:]:
        print(f"Argument {index}: {arg}")
        index += 1

print("Total arguments :", length)
