from medium.combination_sum_ii import combination_sum2


class TestComBinationSum:
    def test_10_1_2_7_6_1_5__8(self):
        actual = combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)
        expect = [[1, 7], [1, 2, 5],
                  [2, 6],
                  [1, 1, 6]]
        print(actual)
        print(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]

        assert set(actual) == set(expect)

    def test_1111_4(self):
        actual = combination_sum2([1, 1, 1, 1], 4)
        expect = [[1, 1, 1, 1]]
        print(actual)
        print(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]

        assert set(actual) == set(expect)

    def test_11111111_8(self):
        actual = combination_sum2([1, 1, 1, 1, 1, 1, 1, 1], 8)
        expect = [[1, 1, 1, 1, 1, 1, 1, 1]]
        print(actual)
        print(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]

        assert set(actual) == set(expect)

    def test_1111111_7(self):
        actual = combination_sum2([1, 1, 1, 1, 1, 1, 1, ], 7)
        expect = [[1, 1, 1, 1, 1, 1, 1, ]]
        print(actual)
        print(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]

        assert set(actual) == set(expect)

    @staticmethod
    def test_2_5_2_1_2__5():
        actual = combination_sum2([2, 5, 2, 1, 2], 5)
        expect = [
            [1, 2, 2],
            [5]
        ]
        print(actual)
        print(expect)
        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]

        assert set(actual) == set(expect)
