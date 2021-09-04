
#  items - list of dictionaries
def field(items, *args):
    assert len(args) > 0
    result = []
    if len(args) == 1:
        for item in items:
            value = item[args[0]]
            if value is not None:
                result.append(value)
    else:
        for item in items:
            new_dict = dict()
            for key_value in args:
                value = item.get(key_value)
                if value is not None:
                    new_dict.update({key_value: value})
            result.append(new_dict)
    return result
