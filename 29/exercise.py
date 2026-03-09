def add_string_numbers(*strings):
    return sum(int(s) for s in strings if s.isdigit())


print(add_string_numbers("10", "abc", "20", "de44", "30", "55fg", "40"))
