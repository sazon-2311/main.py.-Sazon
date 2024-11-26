def get_multiplied_digits (numeber):
    str_number = str(numeber).rstrip("0")
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402030)
print(result)
print(result2)

