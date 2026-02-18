def function():
    """Function that demonstrate automatic vault sealing regardless of
      operation success or failure, with professional security logging
        throughout."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")
    try:
        with open("./classified_data.txt", 'r') as f:
            print(f"{f.read()}\n")
    except FileNotFoundError:
        print("The file 'classified_data.txt' was not found.\n")

    print("SECURE PRESERVATION:")
    with open("security_protocols.txt", 'w') as f:
        f.write("{[}CLASSIFIED{]} New security protocols archived\n")
        f.write("Vault automatically sealed upon completion\n")

    try:
        with open("../security_protocols.txt", 'r') as f:
            print(f"{f.read()}")
    except FileNotFoundError:
        print("The file 'security_protocols.txt' was not found.\n")

    print("All vault operations completed with maximum security.")


function()
