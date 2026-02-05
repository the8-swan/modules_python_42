
def display_content(file_path: str):
    """ Function that accesses the storage unit, extracts all preserved data,
    and displays the recovery process."""
    print("Accessing Storage Vault: ", file_path)
    try:
        f = open(file_path)
        print("Connection established...")
        print("")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    finally:
        print("")
        print("Data recovery complete. Storage unit disconnected")


print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
print("")
display_content("../oumaima.txt")
