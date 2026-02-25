def deepdiff(a, b):
    output = {}
    for key in a.keys() | b.keys():
        if a.get(key) != b.get(key):
            if type(a.get(key)) is dict and type(b.get(key)) is dict:
                output[key] = deepdiff(a.get(key), b.get(key))
            else:
                output[key] = [a.get(key), b.get(key)]

    return output


deepdiff({"a": 1, "b": 2, "c": 3}, {"a": 2, "b": 3, "d": 4})

deepdiff(
    {"a": 1, "b": {"a": 1, "b": 2}, "c": 3}, {"a": 2, "b": {"a": 2, "b": 2}, "d": 4}
)
