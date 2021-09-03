from lab_python_fp import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.sort import lambda_sort
from lab_python_fp.sort import key_sort


def main():
    print("testing")
    goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
             {'title': 'Диван для отдыха', 'price': 5000, 'color': 'black'}
             ]
    #print(field(goods, 'title'))  # output: 'Ковер', 'Диван для отдыха'
    #print(field(goods, 'title', 'price'))
    print(gen_random(5, 1, 3))
    test_array = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    print(key_sort(test_array))
    print(lambda_sort(test_array))


if __name__ == '__main__':
    main()
