def select_and_transform(items, predicate, transform):
    working_set = items
    return_set = []
    for item in working_set:
        if predicate(item):
            return_set.append(transform(item))
    return return_set
