# def min_by_key(key, dict_list):
#     min_val = float('inf')
#     res = {}
#     for d in dict_list:
#         if key in d:
#             if d[key] < min_val:
#                 res = d
#     return res

# def first_by_key(key, direction, dict_list):
#     cmp_dct = {'asc': lambda x,y: x < y, 'desc': lambda x,y: x > y}
#     track_dct = {'asc': float('inf'), 'desc': float('-inf')}
#     min_val = track_dct[direction]
#     res = {}
#     for d in dict_list:
#         cmp = None
#         if key in d:
#             cmp = d[key]
#         else:
#             cmp = 0
#         if cmp_dct[direction](cmp, min_val):
#             res = d
#             min_val = cmp
#     return res


from functools import cmp_to_key
def cmp_generator(key):
    def inner(x, y):
        if key in x and key in y:
            return 0 if x[key] == y[key] else (1 if x[key] > y[key] else -1)
        elif key in x:
            return -1 if x[key] < 0 else 1
        elif key in y:
            return 1 if y[key] < 0 else -1
        return 0
    return inner

def first_by_key(key, direction, dict_list):
    if direction == "asc":
        return min(dict_list, key=cmp_to_key(cmp_generator(key)))
    else:
        return max(dict_list, key=cmp_to_key(cmp_generator(key)))
                   
def min_by_key(key, dict_list):
    return first_by_key(key,"asc", dict_list)
    

assert min_by_key('a', [{'a': 1, 'b': 2}, {'a': 2}]) == {'a': 1, 'b': 2}
assert min_by_key('a', [{'a': 2}, {'a': 1, 'b': 2}]) == {'a': 1, 'b': 2}
assert min_by_key('b', [{'a': 1, 'b': 2}, {'a': 2}]) == {'a': 2}
assert min_by_key('a', [{}]) == {}
assert min_by_key('b', [{'a': -1}, {'b': -1}]) == {'b': -1}

assert first_by_key('a', 'asc', [{'a': 1}]) == {'a': 1}
assert first_by_key('a', 'asc', [{'b': 1}, {'b': -2}, {'a': 10}]) in [{'b': 1}, {'b': -2}]
assert first_by_key('a', 'desc', [{'b': 1}, {'b': -2}, {'a': 10}]) == {'a': 10}
assert first_by_key('b', 'asc', [{'b': 1}, {'b': -2}, {'a': 10}]) == {'b': -2}
assert first_by_key('b', 'desc', [{'b': 1}, {'b': -2}, {'a': 10}]) == {'b': 1}
assert first_by_key('a', 'desc', [{}, {'a': 10, 'b': -10}, {}, {'a': 3, 'c': 3}]) == {'a': 10, 'b': -10}