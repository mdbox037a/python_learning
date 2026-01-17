# not allowed to use sorted() or .sort()
def sort_scores(scores):
    n = len(scores)
    result = []
    i = 0
    while i < n:
        result.append(scores[i])
        i += 1

    length = len(result)
    i = 0
    while i < length:
        j = 0
        while j < length - 1:
            if result[j] > result[j + 1]:
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp
            j += 1
        i += 1

    return result
