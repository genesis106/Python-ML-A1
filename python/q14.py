def read_lines():
    lines = []
    while True:
        line = input("Enter a line (empty line to stop): ")
        if line == "":
            break
        lines.append(line)
    return lines
def printing():
    lines=read_lines()
    for line in lines:
        print(line)
printing()
