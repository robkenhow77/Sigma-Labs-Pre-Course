def digitize(n):
    numbers = list(str(n)[::-1])
    numbers = [int(x) for x in numbers]
    return numbers
