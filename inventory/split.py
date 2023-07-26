def split_lhcc(input_str):
    substrings = input_str.split('^')
    location = substrings[0]
    hall = substrings[1]
    code = substrings[2]
    color = substrings[3]
    return (location, hall, code, color)