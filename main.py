
filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        content = file.readlines()

    error = sum(1 for line in content if "ERROR" in line)
    warning = sum(1 for line in content if "WARNING" in line)
    info = sum(1 for line in content if "INFO" in line)

    print("ERROR:", error)
    print("WARNING:", warning)
    print("INFO:", info)

except FileNotFoundError:
    print("File not found.")
