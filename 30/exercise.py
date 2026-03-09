def flatten_lists(ls):
    if not ls:
        return []
    flattened_items = [item for item in ls if not isinstance(item, list)]
    nested_ls = [item for item in ls if isinstance(item, list)]
    if not nested_ls:
        return flattened_items

    flattened_items.extend(
        [flattened for ls in nested_ls for flattened in flatten_lists(ls)]
    )

    return flattened_items


print(flatten_lists([]))
print(flatten_lists([1, 2, 3, 4]))
print(flatten_lists([1, 2, [3, 4]]))
print(flatten_lists([[1, 2], [3, 4]]))
print(flatten_lists([[1, [2]], [3, 4]]))
print(flatten_lists([[1, [2]], [3, 4, 5], 6, 7, [8, [9, [10]]]]))
