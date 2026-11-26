def normalize(lines):
    return [text for line in lines if (text := line.strip())]
