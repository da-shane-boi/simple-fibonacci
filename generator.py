def get_n(n: int):

    if n < 1:
        return -1
    if n == 1:
        return 0
    if n == 2:
        return 1
    return get_n(n - 1) + get_n(n - 2)


def get_sequence(n: int):

    if n < 1:
        return -1

    seq = []
    if n >= 1:
        seq.append(0)
    if n >= 2:
        seq.append(1)
    for i in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq


def sum_of_sequence(n: int):
    return -1 if n < 1 else sum(get_sequence(n))
