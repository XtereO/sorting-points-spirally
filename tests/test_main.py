from copy import deepcopy
from main import sort_points_spirally


class TestSortingSpirallyAlgorithm:
    def test_empty_points(self):
        points_order = sort_points_spirally([])
        assert points_order == []

    def test_one_point(self):
        points_order = sort_points_spirally([[1, 7, 17]])
        assert points_order == [0]

    def test_picking_pivot_point(self):
        points_order = sort_points_spirally([[-1, 1, 1], [0, 2, 3]])
        assert points_order[0] == 0

        points_order = sort_points_spirally([[0, 2, 3], [-1, 1, 1]])
        assert points_order[0] == 1

        points_order = sort_points_spirally(
            [[-3, 2, 2], [-1, -5, 0], [-3, 1, 5], [7, -3, 5]])
        assert points_order[0] == 2

        points_order = sort_points_spirally( [[-3, 2, 2], [-1, -5, 0], [-3, 2, 5], [7, -3, 5]])
        assert points_order[0] == 0 

        points_order = sort_points_spirally( [[-3, 2, 2], [-1, -5, 0], [-3, 2, 1], [7, -3, 5]])
        assert points_order[0] == 2

        points_order = sort_points_spirally( [[-3, 2, 1], [-1, -5, 0], [-3, 2, 1], [7, -3, 5]])
        assert points_order[0] == 0
    
    def test_two_points(self):
        points_order = sort_points_spirally([[-1, 1, 1], [4, 2, 1]])
        assert points_order == [0, 1]

        points_order = sort_points_spirally([[4, 2, 1], [-1, 1, 1]])
        assert points_order == [1, 0]

    def test_immutable_points(self):
        points = [[-1, 1, 1], [4, 2, 1], [-3, 2, 1], [7, -3, 5]]
        d_points = deepcopy(points)
        points_order = sort_points_spirally(points)
        assert points == d_points

    # what if two dots have the same x and y -> put them together indexes; actually I look for ctg not tg (cause x2-x1 can be equal 0)
        