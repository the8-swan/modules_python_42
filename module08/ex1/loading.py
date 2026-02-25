import importlib
import sys


modules = ["pandas", "requests", "matplotlib", "numpy"]
try:
	print("LOADING STATUS: Loading programs...\n")

	print("Checking dependencies:")
	for module in modules:
		m = importlib.import_module(module)
		print(f"[OK] {module} ({m.__version__})")

except ModuleNotFoundError:
	print("missing dependencies...\n")
	print("To install using pip:\npip install -r requirements.txt\n")
	print("To install using Poetry:\npoetry install\n")