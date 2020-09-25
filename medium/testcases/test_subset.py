from medium.subset import Solution


class TestSubset:
    def test_123(self):
        parameters = [1, 2, 3]
        expect = [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]
        actual = Solution.subsets(parameters)
        assert len(actual) == len(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert set(actual) == set(expect)

    def test_111(self):
        parameters = [1, 1, 1]
        expect = [
            [1],
            [1, 1, 1],
            [1, 1],
            []
        ]
        actual = Solution.subsets(parameters)
        assert len(actual) == len(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert set(actual) == set(expect)