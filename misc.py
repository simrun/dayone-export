# Get a list of all the top level keys
def all_keys(entries):
    keys = set()
    for entry in entries:
        keys = keys | set(entry.keys())
    return keys