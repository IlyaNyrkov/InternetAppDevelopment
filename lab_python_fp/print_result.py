def print_result(func):
    def printing():
        data = func()
        print(func.__name__)
        if type(data) is list:
            for i in data:
                print(i)
        elif type(data) is dict:
            for key, value in data.items():
                print(key, ' = ', value)
        else:
            print(data)
    return printing
