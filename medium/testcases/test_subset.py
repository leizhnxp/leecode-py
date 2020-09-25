import pytest

from medium.subset import Solution

param = [
    ([1, 2, 3], [
        [3],
        [1],
        [2],
        [1, 2, 3],
        [1, 3],
        [2, 3],
        [1, 2],
        []
    ]),
    ([1, 1, 1], [
        [1],
        [1, 1, 1],
        [1, 1],
        []
    ])
]


@pytest.fixture(params=param)
def params(request):
    return request.param


class TestSubset:

    def test_subset(self, params):
        input_ = params[0]
        expect = params[1]
        actual = Solution.subsets(input_)
        assert len(actual) == len(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert set(actual) == set(expect)

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
        print(actual)
        assert len(actual) == len(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert set(actual) == set(expect)
