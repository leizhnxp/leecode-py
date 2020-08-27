import medium.find_sub_dequences as solution


class TestSolution:

    def test_solution_find_sub_sequences_1357(self):
        expect = [[1, 3], [1, 3, 5], [1, 3, 5, 7], [1, 3, 7], [1, 5], [1, 5, 7], [1, 7], [3, 5],
                  [3, 5, 7], [3, 7], [5, 7]]
        actual = solution.Solution.find_sub_sequences([1, 3, 5, 7])

        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]

        assert set(actual) == set(expect)

    def test_solution_find_sub_sequences(self):
        expect = [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7, 7], [4, 7, 7]]
        actual = solution.Solution.find_sub_sequences([4, 6, 7, 7])

        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert set(actual) == set(expect)

    def test_solution_find_sub_seq_4321(self):
        expect = []
        actual = solution.Solution.find_sub_sequences([4, 3, 2, 1])
        assert expect == actual

    def test_solution_find_sub_seq_(self):
        import medium.data.case_data_1234567891011111 as d
        expect = d.CaseData1234567891011111.data
        actual = solution.Solution.find_sub_sequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1])

        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert len(actual) == len(expect)
        assert set(actual) == set(expect)

    def test_110_11111(self):
        expect = [[1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 10]]
        actual = solution.Solution.find_sub_sequences([1, 10, 1, 1, 1, 1])

        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert set(actual) == set(expect)

    def test_1231(self):
        expect = [[1, 1], [1, 2], [1, 3], [1, 2, 3], [2, 3]]
        actual = solution.Solution.find_sub_sequences([1, 2, 3, 1])

        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert set(actual) == set(expect)

    def test_123(self):
        expect = [[1, 2], [1, 3], [1, 2, 3], [2, 3]]
        actual = solution.Solution.find_sub_sequences([1, 2, 3])

        expect = [tuple(x) for x in expect]
        actual = [tuple(x) for x in actual]
        assert set(actual) == set(expect)
