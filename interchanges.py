def get_interchanges(path):
    if not path or len(path) < 2:
        return []

    interchanges = []
    prev_line = path[0].split("~")[-1]

    for i in range(1, len(path)):
        curr_line = path[i].split("~")[-1]
        if curr_line != prev_line:
            interchanges.append((path[i - 1], path[i]))
        prev_line = curr_line

    return interchanges
