import types
from task_1 import logger

@logger
def flat_generator(list_of_lists):
    deep_list = list_of_lists.copy()

    for deep_item in deep_list:
        if not isinstance(deep_item, list):
            deepest_item = deep_item
            yield deepest_item
        elif isinstance(deep_item, list) and len(deep_item) != 0:
            for i in flat_generator(deep_item):
                yield i
        elif isinstance(deep_item, list) and len(deep_item) == 0:
            break


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
