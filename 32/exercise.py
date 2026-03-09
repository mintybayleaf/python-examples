def flipdict(d):
    return {v: k for k, v in d.items()}


print(flipdict({"a": 1, "b": 2, "c": 3}))
