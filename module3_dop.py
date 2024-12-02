data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(args):
    summ = 0
    if isinstance(args, int):
        return args
    if isinstance(args, str):
        return len(args)
    if isinstance(args, dict):
        args = list(args.items())
    for i in args:
        summ = summ + calculate_structure_sum(i)
    return summ



result = calculate_structure_sum(data_structure)

print(result)