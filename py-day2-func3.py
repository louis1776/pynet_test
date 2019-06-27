def open_file(file):
    with open(file) as f:
        return f.read()

def get_serial():
    output = open_file("show_version.txt")
    for line in output.splitlines():
        if "Processor board ID" in line: 
            _, _, _, serial_numb = line.split()
    return serial_numb

print("=======Serial number: {}".format(get_serial()))

