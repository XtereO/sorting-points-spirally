from copy import deepcopy
from utils import pop_by_value


class TestPoppingByValue:
    def test_empty_list(self):
        i = pop_by_value([], "")
        assert i == -1
    
    def test_non_existing_value(self):
        i = pop_by_value([1, 2, 3], 5)
        assert i == -1

    def test_one_item(self):
        i = pop_by_value([1], 1)
        assert i == 0
    
    def test_two_items(self):
        i = pop_by_value([2, 3], 3)
        assert i == 1

        i = pop_by_value(["three", "two"], "three")
        assert i == 0

    def test_mutation_list(self):
        l = [1, 2, 3]
        d_l = deepcopy(l)
        i = pop_by_value(l, 3)
        assert l != d_l
        assert l == [1, 2]

    def test_list_items(self):
        i = pop_by_value([[1, 2], [3, 4], [2, 3]], [3, 4])
        assert i == 1
    
    def test_list_items_mutation(self):
        l = [[1, 2], [7, 4], [2, 3]]
        d_l = deepcopy(l)
        i = pop_by_value(l, [7, 4])
        assert l != d_l
        assert l == [[1, 2], [2, 3]]
    
    def test_case_one(self):
        i = pop_by_value([32, 51, 20, 73, 24, 12], 73)
        assert i == 3
