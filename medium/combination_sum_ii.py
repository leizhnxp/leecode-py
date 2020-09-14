import heapq
import bisect
from typing import List


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:

    result = set()

    for i in range(len(candidates)):
        tmp_groups = []

        for group in result:
            tmp = list(group)
            bisect.insort(tmp, candidates[i])

            if sum(tmp) <= target:
                tmp_groups.append(tuple(tmp))

        result.update(tmp_groups)

        if candidates[i] <= target:
            result.add((candidates[i], ))

    result = [ list(group) for group in result if sum(group) == target]

    return result


if __name__ == '__main__':
    # combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)
    # combination_sum2([2, 5, 2, 1, 2], 3)
    print(combination_sum2([4,1,1,4,4,4,4,2,3,5], 10))
