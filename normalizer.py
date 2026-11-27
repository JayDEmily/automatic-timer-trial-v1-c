def normalize(lines):
    stripped = (line.strip() for line in lines)
    return [line for line in stripped if line]
