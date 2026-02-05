def function():
    """Function that demonstrate automatic vault sealing regardless of
      operation success or failure, with professional security logging
        throughout."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")
    with open("../classified_data.txt", 'r') as f:
        print(f"{f.read()}\n")

    print("SECURE EXTRACTION:")
    with open("../security_protocols.txt", 'r') as f:
        print(f"{f.read()}")
    print("Vault automatically sealed upon completion\n")
    print("")
    print("All vault operations completed with maximum security.")


function()
