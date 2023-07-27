def split_lhcc(input_str):
    substrings = input_str.split('^')
    location = substrings[0]
    code = substrings[1]
    color = substrings[2]
    return (location, code, color)