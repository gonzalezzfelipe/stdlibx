def mean(*args):
    if len(args) == 1:
        args = args[0]
    return sum(args) / len(args)


def perc(it, perc):
    return sorted(it)[floor(len(it) * (perc if perc < 1.0 else perc / 100))]
