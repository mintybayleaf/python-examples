def transform_values(fn, d):
    return {key: fn(value) for key, value in d.items()}


print(transform_values(lambda x: x**2, {"a": 1, "b": 2, "c": 3}))
