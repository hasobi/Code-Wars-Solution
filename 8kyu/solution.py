def abbrevName(name):
    words = name.split()
    letters = [word[0] for word in words]
    return ".".join(letters).upper()
