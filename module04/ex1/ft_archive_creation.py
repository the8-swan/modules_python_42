def function(file_name: str, data: list):
    """Function that displays the system header, storage unit initialization,
    data inscription with numbered entries, and completion confirmation"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("")
    try:
        print("Initializing new storage unit: ", file_name)
        f = open(file_name, 'w')
        print("Storage unit created successfully...")
        print("")
        if data.__len__() != 0:
            print("Inscribing preservation data..")
            for d in data:
                f.write(d + "\n")
                print(d)
        print("")
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive {file_name} ready for long-term preservation.")
        f.close()
    except FileNotFoundError:
        print("Error: directory doesn't exist")
        print("")


data = [
    "{[}ENTRY 001{]} New quantum algorithm discovered",
    "{[}ENTRY 002{]} Efficiency increased by 347%",
    "{[}ENTRY 003{]} Archived by Data Archivist trainee"
]
function("./new_discovery.txt", data)
