import sys
import site
import os

if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS:  You're still plugged in\n")
else:
    print("MATRIX STATUS:  Welcome to the construct\n")

print(f"Current Python: {sys.executable}")


if sys.prefix == sys.base_prefix:
    print("Virtual Environment: NONE detected\n")
    print(
        "WARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n"
    )
    print(
        "To enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\nScripts\nactivate # On Windows\n"
    )

    print("Then run this program again.")
else:
    env_name = os.path.basename(sys.prefix)
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {sys.prefix}\n")
    print(
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n"
    )
    print(f"Package installation path:{site.getsitepackages()[0]}")
