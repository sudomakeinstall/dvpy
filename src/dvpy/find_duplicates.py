def find_duplicates(l):
    return set([_l for _l in l if l.count(_l) > 1])
