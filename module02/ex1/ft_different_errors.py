#!/usr/bin/env python3

def garden_operations(error: str):
    if error == "value":
        num = int("hi")
    elif error == "zero":
        division = 8/0
    elif error == "file":
        open("missing.txt",'r')
    elif error == "key":
        data = {'sws': 30}
        print(data['swan'])

def test_error_types():
    print("testing ValueError")
    try : 
        garden_operations("value")
    except:
        print("Caught ValueError: invalid literal for int()\n")

    print("testing ZeroDivisionError")
    try : 
        garden_operations("zero")
    except:
        print("Caught ZeroDivisionError: division by zero\n")

    print("testing FileNotFoundError")
    try : 
        garden_operations("file")
    except :
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("testing KeyError")
    try : 
        garden_operations("key") 
    except :
        print("Caught KeyError: 'missing swan'\n")

    print("Testing multiple errors together...")
    try :
        garden_operations("value")
        garden_operations("zero")
        garden_operations("file")
        garden_operations("key")
    except :
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")

print("=== Garden Error Types Demo ===\n")
test_error_types()