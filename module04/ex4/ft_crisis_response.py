def function():
    """A function that display crisis alerts for each access attempt,
    appropriate response messages based on error types (FileNotFoundError,
    PermissionError,or other exceptions), status confirmations,
    and overall security completion."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]
    print(f"CRISIS ALERT: Attempting access to {files[0]} ...")
    try:
        with open(files[0]) as f:
            print(f.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

    print(f"CRISIS ALERT: Attempting access to {files[1]} ...")
    try:
        with open(files[1], 'r') as f:
            pass
    except (PermissionError, Exception):
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")

    print(f"CRISIS ALERT: Attempting access to {files[2]} ...")
    try:
        with open(files[2], 'r') as f:
            print(f"SUCCESS: Archive recovered -''{f.read()} ''")
    except Exception:
        print("RESPONSE: Security protocols deny access\n")
    print("STATUS: Crisis handled, security maintained")


function()
