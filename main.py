from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.sort import lambda_sort
from lab_python_fp.sort import key_sort
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1


# functions for decorator tests
@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]

# ==================================================
def main():
    # field method testing
    goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
             {'title': 'Диван для отдыха', 'price': 5000, 'color': 'black'},
             {'title': 'Железный трон', 'price': None, 'color': 'silver'}
             ]
    # output: 'Ковер', 'Диван для отдыха'
    for i in field(goods, 'title'):
        print(i, end=' | ')
    print()
    # output: {'title': 'Ковер', 'price': 2000},
    #         {'title': 'Диван для отдыха', 'price': 5000},
    #         {'title': 'Железный трон'}
    for i in field(goods, 'title', 'price'):
        print(i, end=' | ')
    print()
    # gen_random testing
    quantity_to_gen = 5
    random_nums = gen_random(quantity_to_gen, 1, 3)
    for i in random_nums:
        print(i, end=' ')
    print()
    # sorting functions testing
    test_array = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    print(key_sort(test_array))
    print(lambda_sort(test_array))
    # unique iter testing
    # integer list
    unique_list_it = Unique([1, 1, 1, 1, 1, 1, 2, 2, 2, 2])
    for i in unique_list_it:
        print(i, end=' ')
    # generator
    random_gen_it = Unique(gen_random(10, 1, 3))
    for i in random_gen_it:
        print(i, end=' ')
    print()
    # string list
    string_it = Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'])
    for i in string_it:
        print(i, end=' ')
    print()
    # string list lower case check
    string_case_it = Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], ignore_case=False)
    for i in string_case_it:
        print(i, end=' ')
    print()

    # testing print_result decorator

    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == '__main__':
    main()
