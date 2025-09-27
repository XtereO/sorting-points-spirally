from main import sort_points_spirally 

class TestSortingSpirallyAlgorithm:
    def test_empty_points(self):
        x = sort_points_spirally([])
        assert x == []