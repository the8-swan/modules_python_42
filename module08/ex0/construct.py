import sys
import site
import os

# sys.prefix is the path to the current Python environment
# sys.base_prefix is always the path to the original/global Python
# if they are equal, we are NOT in a virtual environment
if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS:  You're still plugged in\n")
else:
    print("MATRIX STATUS:  Welcome to the construct\n")

# sys.executable gives the full path to the python binary being used
print(f"Current Python: {sys.executable}")


if sys.prefix == sys.base_prefix:
    # no virtual environment detected
    print("Virtual Environment: NONE detected\n")
    print(
        "WARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n"
    )
    # guide the user on how to create and activate a virtual environment
    print(
        "To enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\nScripts\nactivate # On Windows\n"
    )

    print("Then run this program again.")
else:
    # os.path.basename extracts just the folder name from the full path
    # e.g. "/home/user/matrix_env" → "matrix_env"
    env_name = os.path.basename(sys.prefix)
    print(f"Virtual Environment: {env_name}")

    # sys.prefix is the root folder of the active virtual environment
    print(f"Environment Path: {sys.prefix}\n")
    print(
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n"
    )
    # site.getsitepackages() returns a list of folders where packages get installed
    # [0] gives us the main one (usually the lib/pythonX.X/site-packages folder)
    print(f"Package installation path:{site.getsitepackages()[0]}")
