def clip_number(number, min_value = 0, max_value = 1):
    if min_value > max_value:
        min_value, max_value = max_value, min_value

    return max(min(number,max_value), min_value)
